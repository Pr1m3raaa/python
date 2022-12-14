from bot_settings_tg import bot
import random
from aiogram import types
from words import words1
from tg_keyboard import kb_english, kb_english1, kb_english2


async def english(message: types.Message):
    await bot.send_message(message.from_user.id, 'Переведи слово')
    global b
    b = random.choice(list(words1))
    await bot.send_message(message.from_user.id, b, reply_markup=kb_english)
async def english1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Это слово?', reply_markup=kb_english2)
    await bot.send_message(message.from_user.id, words1[b], reply_markup=kb_english2)
async def english4(message: types.Message):
    await bot.send_message(message.from_user.id, 'Запиши. ')
    await bot.send_message(message.from_user.id, words1[b], reply_markup=kb_english1)
    await bot.send_message(message.from_user.id, 'Хочешь ещё одно?')
async def english2(message: types.Message):
    await bot.send_message(message.from_user.id, 'Молодец. Хочешь ещё одно?', reply_markup=kb_english1)
async def english3(message: types.Message):
    await bot.send_message(message.from_user.id, 'Подучи его. Хочешь ещё одно?', reply_markup=kb_english1)





def register_english_handlers(dp):
    dp.register_message_handler(english, commands=['English', 'Хочу'])
    dp.register_message_handler(english1, commands=['Знаю'])
    dp.register_message_handler(english2, commands=['Да'])
    dp.register_message_handler(english3, commands=['Нет'])
    dp.register_message_handler(english4, commands=['Не_знаю'])