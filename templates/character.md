# Персонаж: {Имя}

## Кто это
Роль в шоу, характер, манера держаться, как двигается, как говорит.

## ЯКОРЬ ДЛЯ ПРОМТА (вставлять дословно, не менять ни слова)
```
{Name}, a {age}-year-old {man/woman} with {build}, {hair}, {face details}, wearing {outfit}, {1–2 signature details}.
```

## Голос (если говорит в кадре)
```
speaks in a {low/high}, {calm/energetic} voice with {особенности}
```

## Референсы для Ingredients
- `ref-front.png` — фронтально, нейтральный свет, полный рост/по пояс
- `ref-34.png` — 3/4
- `ref-face.png` — лицо крупно
(хранить в `show/characters/{имя}/`; промт для генерации референса — ниже)

## Промт для генерации референса (Nano Banana / Imagen)
```
Character reference sheet, {ANCHOR}, neutral pose, front view, plain light-grey background, soft even studio lighting, full body, photorealistic.
```

## Чего избегать
Что модель обычно портит у этого персонажа, и как формулировать.
