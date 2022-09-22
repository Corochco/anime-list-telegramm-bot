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