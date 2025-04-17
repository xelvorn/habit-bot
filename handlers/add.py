from telegram import Update
from telegram.ext import CallbackContext
import db

def add(update: Update, context: CallbackContext):
    name = " ".join(context.args)
    if not name:
        update.message.reply_text("Укажи название привычки: /add пить воду")
        return
    db.add_habit(update.effective_user.id, name)
    update.message.reply_text(f"Добавил привычку: {name}")
