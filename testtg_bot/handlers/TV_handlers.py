from aiogram import types
from bot_settings_tg import bot
from tg_keyboard import kb_TV, kb_day, kb_TV_next, find_day_TV
from requests_tg import final_list, ID

chanel_id = 0

async def callback_querry_monday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(1)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_tuesday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(2)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_wensday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(3)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_thursday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(4)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_friday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(5)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_suturday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(6)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)
async def callback_querry_sunday(callback_query: types.CallbackQuery):
    await callback_query.message.answer(final_list(chanel_id, find_day_TV(7)))
    await callback_query.message.answer('Что дальше?', reply_markup=kb_TV_next)


async def callback_querry_next(callback_query: types.CallbackQuery):
    await callback_query.message.answer('На какой?', reply_markup=kb_day)
async def callback_querry_channel_list(callback_query: types.CallbackQuery):
    await callback_query.message.answer('На какой?', reply_markup=kb_TV)


async def TV_channels(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбери канал', reply_markup=kb_TV)


async def Belarus1_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id = ID['Belarus1_id']
async def Belarus2_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id= ID['Belarus2_id']
async def Belarus5_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id = ID['Belarus5_id']
async def ONT_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id= ID['ONT_id']
async def STV_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id = ID['STV_id']
async def NTV_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id = ID['NTV_id']
async def RTR_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)
    global chanel_id
    chanel_id= ID['RTR_id']
async def Mir_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)#Дни нужно выводить инлайн и к дням привязывать функции
    global chanel_id
    chanel_id = ID['MIR_id']
async def Eurosport_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)#Дни нужно выводить инлайн и к дням привязывать функции
    global chanel_id
    chanel_id = ID['Eurosport_id']
async def Eurosport2_day(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_day)#Дни нужно выводить инлайн и к дням привязывать функции
    global chanel_id
    chanel_id = ID['Eurosport2_id']









def register_TV_handler(dp):
    dp.register_callback_query_handler(callback_querry_monday, text='monday_TV')
    dp.register_callback_query_handler(callback_querry_tuesday, text='tuesday_TV')
    dp.register_callback_query_handler(callback_querry_wensday, text='wensday_TV')
    dp.register_callback_query_handler(callback_querry_thursday, text='thursday_TV')
    dp.register_callback_query_handler(callback_querry_friday, text='friday_TV')
    dp.register_callback_query_handler(callback_querry_suturday, text='suturday_TV')
    dp.register_callback_query_handler(callback_querry_suturday, text='sunday_TV')
    dp.register_callback_query_handler(callback_querry_next, text='day')
    dp.register_callback_query_handler(callback_querry_channel_list, text='channel')
    dp.register_message_handler(TV_channels, commands=['Программа'])
    dp.register_message_handler(Belarus1_day, commands=['Беларусь1'])
    dp.register_message_handler(Belarus2_day, commands=['Беларусь2'])
    dp.register_message_handler(Belarus5_day, commands=['Беларусь5'])
    dp.register_message_handler(ONT_day, commands=['ОНТ'])
    dp.register_message_handler(STV_day, commands=['СТВ'])
    dp.register_message_handler(NTV_day, commands=['НТВ'])
    dp.register_message_handler(RTR_day, commands=['Россия24'])
    dp.register_message_handler(Mir_day, commands=['Мир'])
    dp.register_message_handler(Mir_day, commands=['Евросопрт'])
    dp.register_message_handler(Mir_day, commands=['Евроспорт2  '])
