from aiogram import types


button1 = types.KeyboardButton(text='Старт')
button2 = types.KeyboardButton(text='Стоп')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Юзер')
button5 = types.KeyboardButton(text='Рандом')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
#keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#keyboard.add(button1, button2, button3)