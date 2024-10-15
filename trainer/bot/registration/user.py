from aiogram import F, Router
from aiogram.fsm.context import FSMContext

from trainer.bot.def_bot import is_int_and_float
from trainer.bot.replykey_board import button_menu
from trainer.bot.states_group import RegistrationState
from trainer.bot.text import user_registration_text, already_registered, enter_name_text, enter_age_text, \
    enter_height_text, error_age_text, enter_weight_text, error_height_text, enter_average_calories_text, \
    error_weight_text, enter_sleep_time_text, error_average_calories_text, enter_password_text, error_sleep_time_text, \
    finish_registered
from trainer.data_base.def_db import add_db, is_included_db
from trainer.moduls.user_db import User_db

"""

Регистрация пользователя:


class RegistrationState(StatesGroup):
    nickname = State()
    first_name = State()
    age = State()
    height = State()
    weight = State()
    average_calories = State()
    sleep_time = State()
    password = State()

"""

router = Router()


@router.message(F.text == f'{user_registration_text}')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(User_db, message.chat.username)
    button_menu_ = await button_menu(message)
    if is_included:
        await message.answer(f"{already_registered}", reply_markup=button_menu_)
        await state.clear()
    else:
        await message.answer(f'{enter_name_text}')
        await state.set_state(RegistrationState.first_name)


@router.message(RegistrationState.first_name)
async def set_first_name(message, state: FSMContext):
    await state.update_data(nickname=message.chat.username)
    await state.update_data(first_name=message.text)
    await message.answer(f"{enter_age_text}")
    await state.set_state(RegistrationState.age)


@router.message(RegistrationState.age)
async def set_age(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(age=message.text)
        await message.answer(f"{enter_height_text}")
        await state.set_state(RegistrationState.height)
    else:
        await message.answer(f"{error_age_text}")
        await message.answer(f"{enter_age_text}")
        await state.set_state(RegistrationState.age)


@router.message(RegistrationState.height)
async def set_height(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(height=message.text)
        await message.answer(f"{enter_weight_text}")
        await state.set_state(RegistrationState.weight)
    else:
        await message.answer(f"{error_height_text}")
        await message.answer(f"{enter_height_text}")
        await state.set_state(RegistrationState.height)


@router.message(RegistrationState.weight)
async def set_weight(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(weight=message.text)
        await message.answer(f"{enter_average_calories_text}")
        await state.set_state(RegistrationState.average_calories)
    else:
        await message.answer(f"{error_weight_text}")
        await message.answer(f"{enter_weight_text}")
        await state.set_state(RegistrationState.weight)


@router.message(RegistrationState.average_calories)
async def set_average_calories(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(average_calories=message.text)
        await message.answer(f"{enter_sleep_time_text}")
        await state.set_state(RegistrationState.sleep_time)
    else:
        await message.answer(f"{error_average_calories_text}")
        await message.answer(f"{enter_average_calories_text}")
        await state.set_state(RegistrationState.average_calories)


@router.message(RegistrationState.sleep_time)
async def set_sleep_time(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(sleep_time=message.text)
        await message.answer(f"{enter_password_text}")
        await state.set_state(RegistrationState.password)
    else:
        await message.answer(f"{error_sleep_time_text}")
        await message.answer(f"{enter_sleep_time_text}")
        await state.set_state(RegistrationState.sleep_time)


@router.message(RegistrationState.password)
async def set_password(message, state: FSMContext):
    button_menu_ = await button_menu(message)
    await state.update_data(password=message.text)
    data = await state.get_data()
    await add_db(User_db, **data)
    await message.answer(f"{finish_registered}", reply_markup=button_menu_)
    await state.clear()


"""

Конец регестрации

"""
