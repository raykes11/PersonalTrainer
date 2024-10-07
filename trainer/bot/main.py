import asyncio
from trainer.bot.replykey_board import button_start
from trainer.bot.registration.exercise_machine import *
from trainer.bot.registration.trainers import *
from trainer.bot.registration.user import *
from trainer.bot.setting import main, dp
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from trainer.bot.action.set_machine import *
from trainer.bot.action.start_trening import *
from trainer.bot.text import start_text


@dp.message(Command('start'))
async def start_messanges(message):
    await message.answer(f'{start_text}', reply_markup=button_start())

if __name__ == "__main__":
    asyncio.run(main())
