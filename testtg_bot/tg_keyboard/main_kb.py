from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Программа')
b2 = KeyboardButton('/Погода')
b3 = KeyboardButton('/Скидки')
b4 = KeyboardButton('/Новости')
b5 = KeyboardButton('/Цветы')
b6 = KeyboardButton('/English')
kb_mum = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mum.row(b1,b2).row(b3,b4,b5).add(b6)






