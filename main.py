import telebot
from user import User
from telebot import *
from array_users_functions import *

Token = '5689487490:AAHjwCnLYovsV0BA7LpcS7gqz5iisVIUqm8'
bot = telebot.TeleBot(Token)

#commands processing function
@bot.message_handler(commands=['start', 'help', 'show_my_titles', 'add_title'])
def processing_commands(message):
    text = message.text
    id = message.chat.id


#processing text messages
@bot.message_handler(content_types='text')
def processing_text(message):
    text = message.text
    id = message.chat.id

bot.infinity_polling()