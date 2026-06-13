from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("স্বাগতম! 👕 Arafora Shop এ আপনাকে স্বাগতম!\n\nআমাদের কাছে পাবেন সেরা মানের টি-শার্ট। অর্ডার করতে লিখুন /order")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("অর্ডার করতে এই নম্বরে যোগাযোগ করুন:\n📞 01828046204")

app = ApplicationBuilder().token("8824444121:AAGdAQR04Y0v-jH6qJInigfk6OfouzHA72s").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("order", order))
app.run_polling()


