from aiogram import types
from bot_settings_tg import bot
from tg_keyboard import kb_next_weather, kb_weather, help_weather, help_picture, find_day_weather
from requests_tg import combined_text




async def weathers(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой день?', reply_markup=kb_weather)

async def weather_monday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(1)):
        cut_picture = help_picture(find_day_weather(1), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_tuesday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(2)):
        cut_picture = help_picture(find_day_weather(2), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_wensday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(3)):
        cut_picture = help_picture(find_day_weather(3), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_thursday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(4)):
        cut_picture = help_picture(find_day_weather(4), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_friday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(5)):
        cut_picture = help_picture(find_day_weather(5), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_saturday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(6)):
        cut_picture = help_picture(find_day_weather(6), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)
async def weather_sunday(callback: types.CallbackQuery):
    n = 0
    for i in combined_text(find_day_weather(7)):
        cut_picture = help_picture(find_day_weather(7), n)
        help_weather(cut_picture)
        n += 1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                          f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)

async def weather_tomorrow(callback: types.CallbackQuery):
    day = 'tomorrow'
    n = 0
    for i in combined_text(day):
        cut_picture = help_picture(day, n)
        help_weather(cut_picture)
        n+=1
        await bot.send_photo(callback.from_user.id, (open('C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/' \
                                                      f'{cut_picture}.png', "rb")), caption=i)
    await callback.message.answer('Что дальше?', reply_markup=kb_next_weather)

async def other_day(callback: types.CallbackQuery):
    await callback.message.answer('На какой?',reply_markup=kb_weather)
    await callback.answer()





def weather_register_handlers(dp):
    dp.register_message_handler(weathers, commands=['Погода'])
    dp.register_callback_query_handler(weather_monday, text='monday_weather')
    dp.register_callback_query_handler(weather_tuesday, text='tuesday_weather')
    dp.register_callback_query_handler(weather_wensday, text='wensday_weather')
    dp.register_callback_query_handler(weather_thursday, text='thursday_weather')
    dp.register_callback_query_handler(weather_friday, text='friday_weather')
    dp.register_callback_query_handler(weather_saturday, text='suturday_weather')
    dp.register_callback_query_handler(weather_sunday, text='sunday_weather')
    dp.register_callback_query_handler(other_day, text='other_day')
