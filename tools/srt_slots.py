#!/usr/bin/env python3
"""Разбивает субтитры (SRT/VTT) на слоты-сцены длиной не больше N секунд.

Слоты покрывают таймлайн без дыр: от 0 (или --start) до конца последней реплики.
Границы ставятся по границам реплик; реплика длиннее лимита режется на части;
длинные паузы без текста заполняются слотами-перебивками.

Пример:
    python3 tools/srt_slots.py episodes/01-pilot/subtitles.srt -o episodes/01-pilot/slots.md
"""
import argparse
import math
import re
import sys
from dataclasses import dataclass, field

TIME_RE = re.compile(
    r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})\s*-->\s*(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})"
)


@dataclass
class Cue:
    start: float
    end: float
    text: str


@dataclass
class Slot:
    start: float
    end: float
    cues: list = field(default_factory=list)
    note: str = ""


def _secs(h, m, s, ms):
    return int(h or 0) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000


def parse(path):
    with open(path, encoding="utf-8-sig") as f:
        raw = f.read().replace("\r\n", "\n")
    cues = []
    for block in re.split(r"\n\s*\n", raw):
        lines = [l for l in block.strip().split("\n") if l.strip()]
        for i, line in enumerate(lines):
            m = TIME_RE.search(line)
            if m:
                g = m.groups()
                text = " ".join(re.sub(r"<[^>]+>", "", l).strip() for l in lines[i + 1:])
                cues.append(Cue(_secs(*g[:4]), _secs(*g[4:]), text))
                break
    return sorted(cues, key=lambda c: c.start)


def build_slots(cues, max_len, origin):
    slots = []
    cur = Slot(origin, origin)

    def close(at):
        nonlocal cur
        cur.end = at
        slots.append(cur)
        cur = Slot(at, at)

    for cue in cues:
        # Реплика не влезает в текущий слот — закрываем его на старте реплики.
        if cur.cues and cue.end - cur.start > max_len:
            close(min(cue.start, cur.start + max_len))
        # Пауза перед репликой длиннее лимита — слоты-перебивки.
        while cue.start - cur.start > max_len:
            cur.note = "пауза / перебивка"
            close(cur.start + max_len)
        # Реплика сама длиннее лимита — режем на части.
        if cue.end - cur.start > max_len:
            parts = math.ceil((cue.end - cur.start) / max_len)
            step = (cue.end - cur.start) / parts
            for n in range(parts):
                cur.cues.append(cue)
                cur.note = f"длинная реплика, часть {n + 1}/{parts}"
                if n < parts - 1:
                    close(cur.start + step)
            cur.end = cue.end
            continue
        cur.cues.append(cue)
        cur.end = cue.end
    if cur.cues:
        slots.append(cur)
    return slots


def fmt(t):
    m, s = divmod(t, 60)
    return f"{int(m):02d}:{s:04.1f}"


def render(slots, max_len, src):
    out = [
        f"# Слоты по субтитрам: `{src}`",
        "",
        f"Лимит слота: {max_len:g} с. Генерируем по {max_len:g} с, подрезаем до длины слота.",
        "",
        "| # | Таймкод | Длит. | Подрезка | Текст озвучки | Заметка |",
        "|---|---|---|---|---|---|",
    ]
    for i, s in enumerate(slots, 1):
        dur = s.end - s.start
        trim = "весь клип" if dur >= max_len - 0.05 else f"взять {dur:.1f} с"
        seen, texts = set(), []
        for c in s.cues:
            if id(c) not in seen:
                seen.add(id(c))
                texts.append(c.text)
        text = " / ".join(texts).replace("|", "\\|") or "—"
        out.append(f"| S{i:02d} | {fmt(s.start)}–{fmt(s.end)} | {dur:.1f} | {trim} | {text} | {s.note} |")
    total = slots[-1].end - slots[0].start if slots else 0
    out += ["", f"Итого слотов: {len(slots)}, хронометраж: {fmt(total)}"]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subtitles", help="файл .srt или .vtt")
    ap.add_argument("--max", type=float, default=6.0, help="макс. длина слота, с (по умолч. 6)")
    ap.add_argument("--start", type=float, default=0.0, help="начало таймлайна, с (по умолч. 0)")
    ap.add_argument("-o", "--output", help="куда сохранить .md (иначе в stdout)")
    a = ap.parse_args()

    cues = parse(a.subtitles)
    if not cues:
        sys.exit("Не найдено ни одной реплики — проверь формат файла.")
    md = render(build_slots(cues, a.max, a.start), a.max, a.subtitles)
    if a.output:
        with open(a.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Сохранено: {a.output}")
    else:
        print(md, end="")


if __name__ == "__main__":
    main()
