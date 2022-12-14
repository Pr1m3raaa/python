from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


b31 = InlineKeyboardButton('Евпроопт', callback_data='Evroopt')
b32 = InlineKeyboardButton('Доброном', callback_data='Dobronom')
b33 = InlineKeyboardButton('Санта', callback_data='Santa')
b34 = InlineKeyboardButton('Отмена', callback_data='menu')
kb_Shop = InlineKeyboardMarkup(resize_keyboard=True)
kb_Shop.row(b31, b32, b33).add(b34)

bmenu = InlineKeyboardButton('В главное меню', callback_data='menu')
bshop = InlineKeyboardButton('Другой магазин', callback_data='next_shop')
kb_Shop_next = InlineKeyboardMarkup(row_width=1)
kb_Shop_next.add(bshop, bmenu)
