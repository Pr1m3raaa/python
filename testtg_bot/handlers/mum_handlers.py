from aiogram import types, Dispatcher
from tg_keyboard import kb_mum
from bot_settings_tg import bot, dp





async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, мама', reply_markup=kb_mum)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/ForMyMumBot')



async def command_cancel(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, мама', reply_markup=kb_mum)
async def menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Хорошо',reply_markup=kb_mum)
    await callback_query.answer()



def register_handlers_mum(dp):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_cancel, commands=['Отмена'])
    dp.register_callback_query_handler(menu, text='menu')




