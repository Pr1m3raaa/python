from bot_settings_tg import bot
from aiogram import types
from tg_keyboard import kb_Shop, kb_mum, kb_Shop_next
from requests_tg import shop_picture_evroopt, shop_picture_dobronom, shop_picture_santa


async def Shops(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбери магазин', reply_markup=kb_Shop)

async def skidki_dobronom(callback_query: types.CallbackQuery):
    for i in shop_picture_dobronom():
        try:
            await bot.send_photo(callback_query.from_user.id, photo=i)
        except Exception as e:
            print(e)
    await callback_query.message.answer('Что дальше?', reply_markup=kb_Shop_next)
async def skidki_evroopt(callback_query: types.CallbackQuery):
    for i in shop_picture_evroopt():
        try:
            await bot.send_photo(callback_query.from_user.id, photo=i)
        except Exception as e:
            print(e)
    await callback_query.message.answer('Что дальше?', reply_markup=kb_Shop_next)
async def skidki_santa(callback_query: types.CallbackQuery):
    for i in shop_picture_santa():
        try:
            await bot.send_photo(callback_query.from_user.id, photo=i)
        except Exception as e:
            print(e)
    await callback_query.message.answer('Что дальше?', reply_markup=kb_Shop_next)

async def next_shop(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Какой?', reply_markup=kb_Shop)
    await callback_query.answer()



def shop_register_handlers(dp):
    dp.register_message_handler(Shops, commands=['Скидки'])
    dp.register_callback_query_handler(skidki_dobronom, text='Dobronom')
    dp.register_callback_query_handler(skidki_evroopt, text='Evroopt')
    dp.register_callback_query_handler(skidki_santa, text='Santa')
    dp.register_callback_query_handler(next_shop, text='next_shop')