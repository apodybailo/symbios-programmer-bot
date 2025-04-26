import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from openai_logic import handle_message

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", handle_message))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    app.run_polling()
