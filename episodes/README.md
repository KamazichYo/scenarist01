# Эпизоды

Каждый эпизод — папка `NN-slug/` (скопировать `_TEMPLATE/`):

- `script.md` — сценарий от пользователя
- `subtitles.srt` — субтитры озвучки
- `slots.md` — сетка 6-секундных слотов (`python3 tools/srt_slots.py subtitles.srt -o slots.md`)
- `shotlist.md` — шот-лист
- `prompts.md` — готовые промты
