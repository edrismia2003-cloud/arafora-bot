import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("স্বাগতম! Arafora Shop!")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("অর্ডার: 01828046204")

app = ApplicationBuilder().token(os.environ["TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("order", order))
app.run_polling()
