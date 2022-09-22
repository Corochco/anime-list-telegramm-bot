import telebot
from telebot import types
from markups import *

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
