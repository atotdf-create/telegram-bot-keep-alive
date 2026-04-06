import telebot
import os
import time

# User-provided bot token
TOKEN = "8779388737:AAE-sZ*****"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your bot deployed from Manus. I'm now running on GitHub Actions to stay responsive!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == "__main__":
    print("Bot is starting...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(5)
