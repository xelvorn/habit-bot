import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import db, scheduler
from handlers.add import add
from handlers.stats import stats
from handlers.callbacks import mark_done, skip
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

def start(update: Update, context):
    update.message.reply_text(
        "Привет! Я Habit Tracker Bot.\n"
        "Добавь привычку: /add <название>\n"
        "Статистика: /stats"
    )

def daily_reminder(context):
    user_id = context.job.context
    habits = db.get_habits(user_id)
    if not habits:
        return
    buttons = [
        [InlineKeyboardButton(name, callback_data=f"done:{hid}")]
        for hid, name in habits
    ] + [[InlineKeyboardButton("Пропустить всё", callback_data="skip")]]
    kb = InlineKeyboardMarkup(buttons)
    context.bot.send_message(user_id, "Напоминание: отметь сегодня выполненные привычки", reply_markup=kb)

def main():
    db.init_db()
    updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CallbackQueryHandler(mark_done, pattern=r"done:\d+"))
    dp.add_handler(CallbackQueryHandler(skip, pattern="skip"))

    # планировщик
    scheduler.setup_scheduler(updater.job_queue, daily_reminder, None)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
