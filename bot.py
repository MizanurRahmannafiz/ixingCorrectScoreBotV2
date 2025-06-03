import telebot
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো! আমি তোমার Correct Score Prediction Bot।")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    এই বটে তুমি নিচের কমান্ডগুলো ব্যবহার করতে পারো:
/start - বট চালু করার জন্য
/help - সাহায্যের জন্য
    """
    bot.reply_to(message, help_text)

# এখানে আরো prediction logic, API calls ইত্যাদি যুক্ত করবে

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
