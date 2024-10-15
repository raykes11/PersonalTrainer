from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from trainer.bot.replykey_board import button_start
from trainer.bot.text import cancel_text, start_text


router = Router()


@router.message(Command('start'))
async def start_messanges(message):
    await message.answer(f'{start_text}', reply_markup=button_start())

@router.message(Command('cancel'))
async def cancel_messanges(message, state: FSMContext):
    await state.clear()
    await message.answer(f'{cancel_text}', reply_markup=button_start())