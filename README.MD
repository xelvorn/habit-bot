# 📅 Telegram Habit Tracker Bot

Бот для учёта и напоминаний о привычках.

## 🧰 Технологии

- Python 3.11
- python-telegram-bot (JobQueue)
- APScheduler (обёртка в JobQueue)
- SQLite
- Docker, docker-compose
- pytest

## 🚀 Быстрый старт

1. Клонируйте репозиторий
   ```bash
   git clone https://github.com/xelvorn/habit-bot.git
   cd habit-bot
   ```  
2. Скопируйте и заполните `.env` из `.env.example`
3. Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```  
4. Запустите локально  
   ```bash
   python bot.py
   ```  
5. Или через Docker  
   ```bash
   docker-compose up -d
   ```

## 📋 Команды

- `/start` — приветствие  
- `/add <название>` — добавить привычку  
- `/stats` — показать статистику  
- Кнопки “Сделано”/“Пропустить” — отметить выполнение

## ⚙️ Конфигурация

| Переменная      | Описание                      | Пример           |
| --------------- | ----------------------------- | ---------------- |
| BOT_TOKEN       | Токен Telegram‑бота           | `123:ABC`        |
| REMIND_HOUR     | Час напоминаний (0–23)        | `9`              |
| REMIND_MINUTE   | Минуты напоминаний (0–59)     | `0`              |
| DATABASE_URL    | Путь к SQLite базе            | `sqlite:///db.db`|

## 🐳 Docker

```bash
docker build -t habit-bot .
docker run -d --env-file .env habit-bot
```

## 🧪 Тесты

```bash
pytest
```

## 📜 Лицензия

MIT © XELVORN
