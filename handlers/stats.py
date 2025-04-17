from telegram import Update
from telegram.ext import CallbackContext
import db

def stats(update: Update, context: CallbackContext):
    data = db.get_stats(update.effective_user.id)
    if not data:
        update.message.reply_text("Нет привычек или записей.")
        return
    text = "\n".join(
        f"{name}: выполнено {done}/{total}"
        for name, done, total in data
    )
    update.message.reply_text(text)
