import telebot
from telebot import types

Token = '5689487490:AAHjwCnLYovsV0BA7LpcS7gqz5iisVIUqm8'
bot = telebot.TeleBot(Token)

"""#function that show is user in process of registration
def is_in_process_of_registration(id):
    f = open('users.txt', 'r')
    b = False
    line = f.readline()
    while line != '':
        id_now = ''
        for i in range(len(line)):
            if line[i] != '-':
                id_now += line[i]
            else:
                break
        if str(id_now) == str(id):
            print(1)
            if len(line) <= 15:
                print(2)
                b = True
                break
    f.close()
    return b"""

#function with all markups
def markups(number):
    if number == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Show my titles")
        item2 = types.KeyboardButton("Add title")
        item3 = types.KeyboardButton("Rate")
        item4 = types.KeyboardButton("Notes")
        markup.add(item1, item2)
        markup.add(item3, item4)
    elif number == 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Show users rate')
        item2 = types.KeyboardButton('Estimate')
        item4 = types.KeyboardButton('Back')
        item3 = types.KeyboardButton('Change my rates')
        markup.add(item1, item2)
        markup.add(item3, item4)
    elif number == 3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('My notes')
        item2 = types.KeyboardButton('Write notes')
        item3 = types.KeyboardButton('Delete note')
        item4 = types.KeyboardButton('Change note')
        item5 = types.KeyboardButton('Back')
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
    return markup

#function that show local users rating of titles
def show_users_rate(id):
    with open('rating.txt', 'r') as f:
        line = f.readline()
        counter = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Baсk')
        markup.add(item1)
        while line != "":
            counter += 1
            bot.send_message(int(id), line, reply_markup=markup)
            line = f.readline()
        if counter == 0:
            bot.send_message(int(id), 'Oops... I aint have rate now... Sry...', reply_markup=markup)

#function that add titles
def add_title(id, text):
    markup = markups(1)
    with open('add_title.txt', 'r') as f:
        line = f.readline()
        array = []
        while line != '':
            if line[:len(line)-1] != str(id):
                array.append(line)
            line = f.readline()
    with open('add_title.txt', 'w') as f:
        for i in array:
            f.write(str(i))
    with open('user_titles.txt', 'r') as f:
        line = f.readline()
        array = []
        while line != '':
            new_id = line[:line.find('-')]
            if str(new_id) == str(id):
                array.append(line[:len(line)-1] + text + ':')
            else:
                array.append(line)
            line = f.readline()
    with open('user_titles.txt', 'w') as f:
        for i in array:
            f.write(i + '\n')
    bot.send_message(int(id), 'Your title was successfully added!', reply_markup=markup)

#function that show all user titles
def show_titles(id):
    f = open('user_titles.txt', 'r')
    markup = markups(1)
    line = f.readline()
    counter = 0
    while line != '':
        id_now = ''
        for i in range(len(line)):
            if line[i] != '-':
                id_now += line[i]
            else:
                break
        if str(id_now) == str(id):
            title = ''
            counter = 0
            for i in range(line.find('-') + 1, len(line)):
                if line[i] != ':':
                    title += line[i]
                else:
                    counter += 1
                    bot.send_message(int(id), str(title))
                    title = ''
            break
        line = f.readline()
    if counter == 0:
        bot.send_message(int(id), 'U do not have any added titles.', reply_markup=markup)

#function that write nikname to new user
def write_nickname(id, text):
    with open('users.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(str(id) + '-', str(id) + '-' + text + '-' + str(id) + '\n')
    with open('users.txt', 'w') as f:
        f.write(new_data)

#function that show was user registrated or now
def was_user_registrated(id):
    nickname = None
    f = open('users.txt', 'r+') #all lines are like: id-nickname-number_in_exel_table
    line = f.readline()
    while line != '':
        id_now = ''
        for i in range(len(line)):
            if line[i] != '-':
                id_now += line[i]
            else:
                break
        if str(id_now) == str(id):
            nickname = line[line.find('-') + 1:line.rfind('-')]
            break
        line = f.readline()
    if nickname == None:
        f.write(str(id) + '-')
        with open('user_titles.txt', 'r+') as t:
            t.write(str(id) + '-')
    f.close()
    return nickname

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