from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


b110 = InlineKeyboardButton('Понедельник', callback_data='monday_TV')
b111 = InlineKeyboardButton('Вторник', callback_data='tuesday_TV')
b112 = InlineKeyboardButton('Среда', callback_data='wensday_TV')
b113 = InlineKeyboardButton('Четверг', callback_data='thursday_TV')
b114 = InlineKeyboardButton('Пятница', callback_data='friday_TV')
b115 = InlineKeyboardButton('Суббота', callback_data='suturday_TV')
b116 = InlineKeyboardButton('Воскресенье', callback_data='sunday_TV')
b117 = InlineKeyboardButton('В главное меню', callback_data='menu')
kb_day = InlineKeyboardMarkup(resize_keyboard=True)
kb_day.add(b110,b111,b112).row(b113,b114).row(b115,b116).add(b117)

b1next = InlineKeyboardButton('На другой день', callback_data='day')
b1home = InlineKeyboardButton('В меню каналов', callback_data='channel')
kb_TV_next = InlineKeyboardMarkup(resize_keyboard=True)
kb_TV_next.add(b1next,b1home)



b11 = KeyboardButton('/Беларусь1')
b12 = KeyboardButton('/ОНТ')
b13 = KeyboardButton('/Беларусь5')
b14 = KeyboardButton('/НТВ')
b15 = KeyboardButton('/СТВ')
b16 = KeyboardButton('/Россия24')
b17 = KeyboardButton('/Мир')
b18 = KeyboardButton('/Беларусь2')
b19 = KeyboardButton('/Евроспорт')
b20 = KeyboardButton('/Евроспорт2')
b21 = KeyboardButton('/Отмена')
kb_TV = ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
kb_TV.row(b11,b12).row(b13,b14,b15).row(b16,b17,b18).row(b19,b20).add(b21)