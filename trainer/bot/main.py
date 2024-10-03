import asyncio
import logging
import sys
from sqlalchemy.orm import Session
from trainer.bot.replykey_board import *
from trainer.bot.registration.exercise_machine import *
from trainer.bot.registration.trainers import *
from trainer.bot.registration.user import *
from trainer.bot.setting import main, dp
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from trainer.bot.action.set_machine import *
from trainer.bot.action.start_trening import *

answer_db1 = []


@dp.message(Command('start'))
async def start_messanges(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=button_start())


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
