from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b61 = KeyboardButton('/Знаю')
b62 = KeyboardButton('/Не_знаю')
kb_english = ReplyKeyboardMarkup(resize_keyboard=True)
kb_english.add(b61,b62)

b63 = KeyboardButton('/Хочу')
b64 = KeyboardButton('/Отмена')
kb_english1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_english1.add(b63,b64)

bYes = ('/Да')
bNo = ('/Нет')
kb_english2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_english2.add(bNo,bYes)