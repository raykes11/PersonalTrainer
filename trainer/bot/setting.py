import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from trainer.bot.api import API

api = API
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot, skip_updates=True)
