from aiogram import F
from aiogram.fsm.context import FSMContext

from trainer.bot.replykey_board import *
from trainer.bot.setting import dp
from trainer.bot.states_group import GetMachine
from trainer.bot.text import already_not_registered, muscle_selection_text, choose_muscle_text, one_set_trening_text, \
    two_set_trening_text, three_set_trening_text, one_set_repetition_text, two_set_repetition_text, \
    tree_set_repetition_text, add_machine_complite_text
from trainer.data_base.def_db import get_db_machine_where_title, set_trening, is_included_db
from trainer.moduls.user_db import User_db

"""

Добовление тренажера в набор тренировки

class GetMachine(StatesGroup):
    group_muscles = State()
    title_machin = State()
    list_weight = State()
    set_1_weight = State()
    set_2_weight = State()
    set_3_weight = State()
    iter_1 = State()
    iter_2 = State()
    iter_3 = State()
    machin = State()
    
"""

@dp.message(F.text == f'{add_machine_text}')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(User_db, message.chat.username)
    if not is_included:
        await message.answer(f"{already_not_registered}", reply_markup=button_start())
        await state.clear()
    else:
        await message.answer(f'{muscle_selection_text}', reply_markup=muscle_group)
        await state.set_state(GetMachine.group_muscles)


@dp.message(GetMachine.group_muscles)
async def set_age(message, state: FSMContext):
    keyboard = await button_spesific_muscule(message.text)
    await state.update_data(group_muscles=message.text)
    await message.answer(f"{choose_muscle_text}", reply_markup=keyboard)
    await state.set_state(GetMachine.title_machin)


@dp.message(GetMachine.title_machin)
async def set_age(message, state: FSMContext):
    title = await get_db_machine_where_title(message.text)
    await state.update_data(machin=title)
    await message.answer(f"{one_set_trening_text}", reply_markup=button_list_weight(title['list_weight']))
    await state.set_state(GetMachine.set_1_weight)


@dp.message(GetMachine.set_1_weight)
async def set_age(message, state: FSMContext):
    await state.update_data(set_1_weight=message.text)
    title = await state.get_data()
    await message.answer(f"{two_set_trening_text}",
                         reply_markup=button_list_weight(title['machin']['list_weight']))
    await state.set_state(GetMachine.set_2_weight)


@dp.message(GetMachine.set_2_weight)
async def set_age(message, state: FSMContext):
    await state.update_data(set_2_weight=message.text)
    title = await state.get_data()
    await message.answer(f"{three_set_trening_text}",
                         reply_markup=button_list_weight(title['machin']['list_weight']))
    await state.set_state(GetMachine.set_3_weight)


@dp.message(GetMachine.set_3_weight)
async def set_age(message, state: FSMContext):
    await state.update_data(set_3_weight=message.text)
    await message.answer(f"{one_set_repetition_text}", reply_markup=button_number())
    await state.set_state(GetMachine.iter_1)


@dp.message(GetMachine.iter_1)
async def set_age(message, state: FSMContext):
    await state.update_data(iter_1=message.text)
    await message.answer(f"{two_set_repetition_text}", reply_markup=button_number())
    await state.set_state(GetMachine.iter_2)


@dp.message(GetMachine.iter_2)
async def set_age(message, state: FSMContext):
    await state.update_data(iter_2=message.text)
    await message.answer(f"{tree_set_repetition_text}", reply_markup=button_number())
    await state.set_state(GetMachine.iter_3)


@dp.message(GetMachine.iter_3)
async def set_age(message, state: FSMContext):
    button_menu_ = await button_menu(message)
    await state.update_data(iter_3=message.text)
    title = await state.get_data()
    up_data = {}
    up_data[f"{title['group_muscles']}-{title['machin']['title']}"] = [
        [title['set_1_weight'], title['set_2_weight'], title['set_3_weight']],
        [title['iter_1'], title['iter_2'], title['iter_3']]]
    await set_trening(message.chat.username, up_data)
    await state.clear()
    await message.answer(f"{add_machine_complite_text}", reply_markup=button_menu_)
