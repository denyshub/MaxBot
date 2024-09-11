import os
import subprocess
import requests
from bs4 import BeautifulSoup
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters
from urllib.parse import urljoin

bot_token = ""
chat_id = ""  # Вкажи правильний chat_id
bot = Bot(token=bot_token)

url = ""

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


async def write_image():
    # тут вкажи якісь унікальні ознаки тої фотки
    alt_ = ""

    images = soup.find_all("img", alt=alt_)

    if images:
        img = images[0]
        img_url = img.get("src")
        img_url = urljoin(url, img_url)
        print(f"Image URL: {img_url}")  # Додаткове логування

        try:
            image_response = requests.get(img_url)
            image_response.raise_for_status()  # Перевіряємо на помилки при запиті

            with open("downloaded_image.jpg", "wb") as file:
                file.write(image_response.content)

            print("Image successfully saved.")  # Логування успіху
        except requests.RequestException as e:
            print(f"Failed to fetch image: {e}")
            raise Exception("Image_process_failed")
    else:
        print("No matching images found.")
        raise Exception("Image_process_failed")


async def get_and_send_image():
    # Відкриваємо зображення та надсилаємо його
    with open("downloaded_image.jpg", "rb") as image_file:
        # Використовуємо await для асинхронного виклику
        await bot.send_photo(chat_id=chat_id, photo=image_file)


# Логіка для обробки певного слова
async def handle_message(update: Update, context):
    message_text = update.message.text

    if message_text.lower() == "фото":
        # Видаляємо файл, якщо він існує
        file_path = "downloaded_image.jpg"
        if os.path.exists(file_path):
            os.remove(file_path)
            await update.message.reply_text(f"Файл {file_path} оновлюється.")
        else:
            await update.message.reply_text(f"Файл {file_path} не знайдено.")

        # Виконуємо скрипт parser.py
        try:
            await write_image()
            await update.message.reply_text("Скрипт parser.py виконано!")
            await get_and_send_image()  # Додаємо await, щоб дочекатися завершення відправки
        except Exception as e:
            await update.message.reply_text(f"Помилка під час виконання: {str(e)}")
    else:
        await update.message.reply_text(f"Ви написали: {message_text}")


if __name__ == "__main__":
    # Створюємо додаток
    application = Application.builder().token(bot_token).build()

    # Додаємо обробник для текстових повідомлень
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Запускаємо бота
    application.run_polling()
