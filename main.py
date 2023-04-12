from aiogram import Dispatcher, Bot, executor
import asyncio
import random
from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN,parse_mode="HTML")
dp = Dispatcher(bot, loop=loop,storage=storage)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, loop=loop)



