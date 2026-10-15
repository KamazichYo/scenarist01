# scenarist01

Рабочая зона сценариста-раскадровщика: сценарий + субтитры → сцены по 6 секунд →
детальные промты для **Gemini Omni Flash** в **Google Flow**.

- Роль и правила — [`CLAUDE.md`](CLAUDE.md)
- База знаний по промтингу — [`knowledge/`](knowledge/)
- Библия шоу, персонажи, локации — [`show/`](show/)
- Шаблоны — [`templates/`](templates/)
- Эпизоды — [`episodes/`](episodes/)
- Разбивка субтитров на слоты: `python3 tools/srt_slots.py subtitles.srt -o slots.md`

Скилы Claude Code: `/breakdown` (весь эпизод), `/shot-prompt` (одна сцена / правка).
