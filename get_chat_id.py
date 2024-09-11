from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# Токен твого бота
bot_token = "7121777128:AAFWq_9NufNjJZP2EuDwgQllvquVD9FWbLU"


async def get_chat_id(update: Update, context):
    # Отримуємо ID чату
    chat_id = update.message.chat_id
    # Відправляємо його в чат
    await update.message.reply_text(f"Your chat ID is: {chat_id}")


if __name__ == "__main__":
    # Створюємо додаток
    application = Application.builder().token(bot_token).build()

    # Додаємо обробник для текстових повідомлень
    application.add_handler(MessageHandler(filters.TEXT, get_chat_id))

    # Запускаємо бота
    application.run_polling()
