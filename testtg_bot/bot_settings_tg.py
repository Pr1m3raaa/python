from aiogram import Bot
from aiogram.dispatcher import Dispatcher as dis
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp= dis(bot, storage=storage)