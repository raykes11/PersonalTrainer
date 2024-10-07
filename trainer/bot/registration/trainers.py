from aiogram import F
from aiogram.fsm.context import FSMContext

from trainer.bot.def_bot import is_int_and_float
from trainer.bot.replykey_board import button_menu
from trainer.bot.setting import dp
from trainer.bot.states_group import Trainer
from trainer.bot.text import already_registered, enter_name_text, enter_age_text, \
    enter_height_text, error_age_text, enter_weight_text, error_height_text, enter_average_calories_text, \
    error_weight_text, enter_sleep_time_text, error_average_calories_text, about_self, error_sleep_time_text, \
    enter_password_text, finish_registered, training_registration_text
from trainer.data_base.def_db import add_db, is_included_db
from trainer.moduls.trainers_db import Trainer_db
from trainer.moduls.user_db import User_db

"""

Регистрация тренера:


class Trainer(StatesGroup):
    nickname = State()
    first_name = State()
    about_self = State()
    age = State()
    height = State()
    weight = State()
    average_calories = State()
    sleep_time = State()
    password = State()
    trainer = State()

"""


@dp.message(F.text == f'{training_registration_text}')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(Trainer_db, message.chat.username)
    button_menu_ = await button_menu(message)
    if is_included:
        await message.answer(f"{already_registered}", reply_markup=button_menu_)
        await state.clear()
    else:
        await message.answer(f'{enter_name_text}')
        await state.set_state(Trainer.first_name)


@dp.message(Trainer.first_name)
async def set_first_name(message, state: FSMContext):
    await state.update_data(nickname=message.chat.username)
    await state.update_data(first_name=message.text)
    await message.answer(f"{enter_age_text}")
    await state.set_state(Trainer.age)


@dp.message(Trainer.age)
async def set_age(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(age=message.text)
        await message.answer(f"{enter_height_text}")
        await state.set_state(Trainer.height)
    else:
        await message.answer(f"{error_age_text}")
        await message.answer(f"{enter_age_text}")
        await state.set_state(Trainer.age)


@dp.message(Trainer.height)
async def set_height(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(height=message.text)
        await message.answer(f"{enter_weight_text}")
        await state.set_state(Trainer.weight)
    else:
        await message.answer(f"{error_height_text}")
        await message.answer(f"{enter_height_text}")
        await state.set_state(Trainer.height)


@dp.message(Trainer.weight)
async def set_weight(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(weight=message.text)
        await message.answer(f"{enter_average_calories_text}")
        await state.set_state(Trainer.average_calories)
    else:
        await message.answer(f"{error_weight_text}")
        await message.answer(f"{enter_weight_text}")
        await state.set_state(Trainer.weight)


@dp.message(Trainer.average_calories)
async def set_average_calories(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(average_calories=message.text)
        await message.answer(f"{enter_sleep_time_text}")
        await state.set_state(Trainer.sleep_time)
    else:
        await message.answer(f"{error_average_calories_text}")
        await message.answer(f"{enter_average_calories_text}")
        await state.set_state(Trainer.average_calories)


@dp.message(Trainer.sleep_time)
async def set_sleep_time(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(average_calories=message.text)
        await message.answer(f"{about_self}")
        await state.set_state(Trainer.about_self)
    else:
        await message.answer(f"{error_sleep_time_text}")
        await message.answer(f"{enter_sleep_time_text}")
        await state.set_state(Trainer.sleep_time)


@dp.message(Trainer.about_self)
async def set_about_self(message, state: FSMContext):
    await state.update_data(about_self=message.text)
    await message.answer(f"{enter_password_text}")
    await state.set_state(Trainer.password)


@dp.message(Trainer.password)
async def set_password(message, state: FSMContext):
    button_menu_ = await button_menu(message)
    await state.update_data(password=message.text)
    data = await state.get_data()
    await add_db(Trainer_db, **data)
    is_included = await is_included_db(User_db, message.chat.username)
    if not is_included:
        await add_db(User_db, **data)
    await message.answer(f"{finish_registered}", reply_markup=button_menu_)
    await state.clear()


"""

Конец регестрации

"""
