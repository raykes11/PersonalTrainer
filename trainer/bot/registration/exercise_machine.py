from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from trainer.bot.def_bot import step_calculation, valid_setting, valid_muscular, is_int_and_float
from trainer.bot.replykey_board import muscle_group, button_menu, button_start
from trainer.bot.states_group import ExerciseMachine
from trainer.bot.text import already_registered, creating_machine, add_title_texs, error_title_text, \
    creat_mass_list_tesx, example_4_parametr_text, example_5_parametr_text, muscle_selection_text, extra_weight_text, \
    error_extra_weight_text, count_extra_weight_text, finish_registered
from trainer.data_base.def_db import add_db, is_included_db, is_included_db_machine
from trainer.moduls.exercise_machine_db import ExerciseMachine_db
from trainer.moduls.user_db import User_db

"""

Создание тренажера:

class ExerciseMachine(StatesGroup):
    user_create = State()
    title = State()
    max_weight = State()
    min_weight = State()
    add_weight = State()
    add_weight_item = State()
    list_weight = State()
    group_muscles = State()


"""

router = Router()


@router.message(F.text == f'{creating_machine}')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(User_db, message.chat.username)
    if not is_included:
        await message.answer(f"{already_registered}", reply_markup=button_start())
        await state.clear()
    else:
        await message.answer(f'{add_title_texs}')
        await state.set_state(ExerciseMachine.title)


@router.message(ExerciseMachine.title)
async def set_username(message, state: FSMContext):
    is_included = await is_included_db_machine(message.text)
    if is_included:
        await message.answer(f"{error_title_text}")
        await message.answer(f'{add_title_texs}')
        await state.set_state(ExerciseMachine.title)
    else:
        await state.update_data(user_create=message.chat.username)
        await state.update_data(title=message.text)
        await message.answer(
            f"{creat_mass_list_tesx}")
        await message.answer(f"<i>{example_4_parametr_text}</i>", parse_mode=ParseMode.HTML)
        await message.answer(f"<i>{example_5_parametr_text}</i>", parse_mode=ParseMode.HTML)
        await state.set_state(ExerciseMachine.list_weight)


@router.message(ExerciseMachine.list_weight)
async def set_age(message, state: FSMContext):
    if valid_setting(message.text):
        list_weight = step_calculation(message.text)
        await state.update_data(list_weight=str(list_weight), min_weight=list_weight[0], max_weight=list_weight[-1])
        await message.answer(f"{muscle_selection_text}", reply_markup=muscle_group)
        await state.set_state(ExerciseMachine.group_muscles)
    else:
        await message.answer(
            f"{creat_mass_list_tesx}")
        await message.answer(f"<i>{example_4_parametr_text}</i>", parse_mode=ParseMode.HTML)
        await message.answer(f"<i>{example_5_parametr_text}</i>", parse_mode=ParseMode.HTML)
        await state.set_state(ExerciseMachine.list_weight)


@router.message(ExerciseMachine.group_muscles)
async def set_age(message, state: FSMContext):
    if valid_muscular(message.text):
        await state.update_data(group_muscles=message.text)
        await message.answer(f"{extra_weight_text}")
        await state.set_state(ExerciseMachine.add_weight)
    else:
        await message.answer(f"{muscle_selection_text}", reply_markup=muscle_group, )
        await state.set_state(ExerciseMachine.group_muscles)


@router.message(ExerciseMachine.add_weight)
async def set_age(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(add_weight=message.text)
        await message.answer(f"{count_extra_weight_text}")
        await state.set_state(ExerciseMachine.add_weight_item)
    else:
        await message.answer(f"{error_extra_weight_text}")
        await message.answer(f"{extra_weight_text}")
        await state.set_state(ExerciseMachine.add_weight)


@router.message(ExerciseMachine.add_weight_item)
async def set_age(message, state: FSMContext):
    button_menu_ = await button_menu(message)
    if is_int_and_float(message.text):
        await state.update_data(add_weight_item=message.text)
        data = await state.get_data()
        await add_db(ExerciseMachine_db, **data)
        await message.answer(f"{finish_registered}", reply_markup=button_menu_)
        await state.clear()
    else:
        await message.answer(f"{count_extra_weight_text}")
        await state.set_state(ExerciseMachine.add_weight_item)


"""

Конец регестрации

"""
