from bot_settings_tg import bot, dp
from aiogram.utils import executor
from handlers import mum_handlers, Shop_handlers, TV_handlers, english_handlers,weather_handlers

async def on_start(_):
    print('Онлайн')

mum_handlers.register_handlers_mum(dp)
Shop_handlers.shop_register_handlers(dp)
TV_handlers.register_TV_handler(dp)
english_handlers.register_english_handlers(dp)
weather_handlers.weather_register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)