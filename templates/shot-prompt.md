# Шаблон карточки сцены

````markdown
### S{NN} · {00:00.0–00:06.0} · {короткое название}

**Озвучка (из субтитров):** «...»
**Что видим / зачем:** 1–2 предложения по-русски — смысл кадра, связь с текстом.
**Режим Flow:** Text-to-Video | Frames (первый кадр: ...) | Ingredients
**Референсы:** {Персонаж: show/characters/..}, {Локация: show/locations/..}
**Подрезка:** весь клип | взять 0–4 с
**Переход к следующей:** склейка / по движению / по звуку

```
{CAMERA: shot size + movement}, single continuous shot, no cuts.
{STYLE ANCHOR}. {LIGHTING}. {LOCATION ANCHOR}.
{CHARACTER ANCHOR — дословно из карточки}
{ACTION — одно ясное действие, глаголами, с привязкой ко времени при необходимости}.
Audio: {SFX / ambience}. No dialogue, no voiceover, no music.
No subtitles, no on-screen text, no logos.
```
````

## Вариант с репликой в кадре

```
Medium close-up, static, single continuous shot, no cuts. {STYLE}. {LIGHT}. {LOCATION}.
{CHARACTER ANCHOR} looks into the camera and says in a {тембр/интонация} voice, in Russian: "{реплика ≤ ~5 с}".
Audio: {эмбиент тихо под голосом}. No music. Only this one line of dialogue.
No subtitles, no on-screen text.
```

## Вариант с битами (склейка внутри клипа)

```
{STYLE}. {LIGHT}. {LOCATION}. {CHARACTER ANCHOR}
[00:00-00:03] Close-up, ... SFX: ...
[00:03-00:06] Cut to wide shot, ... SFX: ...
No dialogue, no music. No on-screen text.
```

## Правка готового клипа (режим редактирования Flow)

```
Change only the following:
1. ...
2. ...
Keep everything else identical — same character, same framing, same timing, same audio.
```
