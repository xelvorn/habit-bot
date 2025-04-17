from telegram import CallbackQuery
from telegram.ext import CallbackContext
import db
from datetime import date

def mark_done(update: CallbackQuery, context: CallbackContext):
    habit_id = int(update.data.split(":")[1])
    today = date.today().isoformat()
    db.add_record(habit_id, today, True)
    update.answer("Отметил выполненным ✅")

def skip(update: CallbackQuery, context: CallbackContext):
    update.answer("Пропущено ⏭️")
