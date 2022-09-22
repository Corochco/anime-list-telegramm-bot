import telebot
from telebot import types
from functions import *
from markups import *
Token = '5689487490:AAHjwCnLYovsV0BA7LpcS7gqz5iisVIUqm8'
bot = telebot.TeleBot(Token)

#commands processing function
@bot.message_handler(commands=['start', 'help', 'show_my_titles', 'add_title'])
def processing_commands(message):
    text = message.text
    id = message.chat.id
    markup = markups(1)
    if text == '/start':
        nickname = was_user_registrated(id)
        if nickname != None:
            bot.send_message(id, 'Hello again, ' + nickname, reply_markup=markup)
        else:
            bot.send_message(id, "Hello! I see u aint here! Lets start registration! Write your nickname.")
    elif text == '/help':
        bot.send_message(message.chat.id, 'Welcome! This bot can help you make a library of anime you have watched and write/read reviews about them.', reply_markup=markup)

#processing text messages
@bot.message_handler(content_types='text')
def processing_text(message):
    text = message.text
    id = message.chat.id
    markup = markups(1)
    #is user in process of registration?
    registrate = 1 if was_user_registrated(id) == '' else 0
    if registrate:
        write_nickname(id, text)
        bot.send_message(message.chat.id, 'Your nickname is saved! Enjoy using the bot!', reply_markup=markup)
    #is user in process of add title?
    with open('add_title.txt', 'r') as f:
        line = f.readline()
        b = False
        while line != '':
            if str(line[:len(line)-1]) == str(id):
                b = True
            line = f.readline()
    if b:
        add_title(id, message.text)
    if text == 'Show my titles':
        show_titles(id)
    elif text == 'Add title':
        bot.send_message(id, 'Write name of the title, that u wanna add.', reply_markup=None)
        with open('add_title.txt', 'r+') as f:
            f.write(str(id) + '\n')
    elif text == 'Rate':
        markup = markups(2)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Show users rate':
        show_users_rate(id)
    elif text == 'Notes':
        markup = markups(3)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Back':
        markup = markups(1)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    #this back from notes
    elif text == 'Bаck':
        markup = markups(3)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    #this back from rate
    elif text == 'Baсk':
        markup = markups(2)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Estimate':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Baсk')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Change my rates':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Baсk')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'My notes':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Bаck')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Write notes':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Bаck')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Delete note':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Bаck')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)
    elif text == 'Change note':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Bаck')
        markup.add(item)
        bot.send_message(int(id), '-_-', reply_markup=markup)

bot.infinity_polling()