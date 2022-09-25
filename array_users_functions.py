from user import User
def string_to_array(line):
    id, nickname, title_string, rate_string, note_string = map(str, line.split(','))
    title_array = []
    counter = len(title_string)
    #заполняем массив тайтлов
    for i in range(counter):
        if i % 2 == 0:
            elem1 = title_string[:title_string.find('-')]
            title_string = title_string[title_string.find('-') + 1:]
        else:
            elem2 = title_string[:title_string.find('-')]
            title_string = title_string[title_string.find('-') + 1:]
            title_array.append([elem1, elem2])
            elem1, elem2 = '', ''
    rate_array = []
    #заполняем массив рэйтинга
    for i in range(counter):
        if i % 2 == 0:
            elem1 = rate_string[:rate_string.find('-')]
            rate_string = rate_string[rate_string.find('-') + 1:]
        else:
            elem2 = rate_string[:rate_string.find('-')]
            rate_string = rate_string[rate_string.find('-') + 1:]
            rate_array.append([elem1, elem2])
            elem1, elem2 = '', ''
    note_array = []
    #заполняем массив отзывов
    for i in range(counter):
        if i % 2 == 0:
            elem1 = note_string[:note_string.find('-')]
            note_string = note_string[note_string.find('-') + 1:]
        else:
            elem2 = note_string[:note_string.find('-')]
            note_string = note_string[note_string.find('-') + 1:]
            note_array.append([elem1, elem2])
            elem1, elem2 = '', ''
    user = User(id, nickname, title_array, rate_array, note_array)
    return user

def get_all_users_array():
    try:
        with open('users.txt', 'r') as f:
            line = f.readline()
            array = []
            while line != '':
                new_elem = string_to_array(line)
                array.append(new_elem)
        return array
    except FileNotFoundError:
        print('Невозможно открыть файл users.txt, тк он не существует в данной дирректории.')