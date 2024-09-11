## Steps to Run the Project

1. **Clone the Project from GitHub**

   - Create any folder.
   - Navigate to it and run:
     ```bash
     git clone https://github.com/denyshub/MaxBot.git
     ```
     - Install all requirements
     ```bash
      pip install -r requirements.txt
     ```

2. **Get chat id**

   - Find the line bot_token = 'YOUR_BOT_TOKEN' and replace 'YOUR_BOT_TOKEN' with your bot's token received from BotFather.
   - Run get_chat_id.py:
     ```bash
     python get_chat_id.py
     ```
   - Open Telegram and send any message to bot, recieve your chat id.
   - Cntl + C in terminal to stop the bot.

3. **Set up bot for your needs**

   - Open tgbot.py
   - Find the line bot_token = 'YOUR_BOT_TOKEN' and replace 'YOUR_BOT_TOKEN' with your bot's token received from BotFather.
   - In write_image() insert the features by which you want to parse photos.

4. **Start the bot**
   - Run get_chat_id.py:
   ```bash
   python tgbot.py
   ```
   - Send assigned message to get image.
