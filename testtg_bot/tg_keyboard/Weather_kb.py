from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

b20 = InlineKeyboardButton('Понедельник', callback_data='monday_weather')
b21 = InlineKeyboardButton('Вторник', callback_data='tuesday_weather')
b22 = InlineKeyboardButton('Среда', callback_data='wensday_weather')
b23 = InlineKeyboardButton('Четверг', callback_data='thursday_weather')
b24 = InlineKeyboardButton('Пятница', callback_data='friday_weather')
b25 = InlineKeyboardButton('Суббота', callback_data='suturday_weather')
b26 = InlineKeyboardButton('Воскресенье', callback_data='sunday_weather')
b27 = InlineKeyboardButton('В главное меню', callback_data='menu')
kb_weather = InlineKeyboardMarkup()
kb_weather.add(b20,b21,b22).row(b23,b24).row(b25,b26).add(b27)

b01= InlineKeyboardButton('На другой день', callback_data='other_day')
b02=InlineKeyboardButton('В главное меню', callback_data='menu')
kb_next_weather = InlineKeyboardMarkup()
kb_next_weather.add(b01,b02)