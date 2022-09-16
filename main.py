import telebot

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

#function that add titles
def add_title(id, text):
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
            f.write(i)
    bot.send_message(int(id), 'Your title was successfully added!')

#function that show all user titles
def show_titles(id):
    f = open('user_titles.txt', 'r')
    line = f.readline()
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
        bot.send_message(int(id), 'U do not have any added titles.')

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
    if text == '/start':
        nickname = was_user_registrated(id)
        if nickname != None:
            bot.send_message(id, 'Hello again, ' + nickname)
        else:
            bot.send_message(id, "Hello! I see u aint here! Lets start registration! Write your nickname.")
    elif text == '/help':
        bot.send_message(message.chat.id, 'Welcome! This bot can help you make a library of anime you have watched and write/read reviews about them. If u wanna see all your titles, use command /show_my_titles. If u wanna add titles, write /add_title.')
    elif text == '/show_my_titles':
        show_titles(id)
    elif text == '/add_title':
        bot.send_message(id, 'Write name of the title, that u wanna add.')
        with open('add_title.txt', 'r+') as f:
            f.write(str(id) + '\n')

#processing text messages
@bot.message_handler(content_types='text')
def processing_text(message):
    text = message.text
    id = message.chat.id
    #is user in process of registration?
    registrate = 1 if was_user_registrated(id) == '' else 0
    if registrate:
        write_nickname(id, text)
        bot.send_message(message.chat.id, 'Your nickname is saved! Enjoy using the bot!')
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

bot.infinity_polling()