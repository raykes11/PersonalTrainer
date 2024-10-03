from aiogram import F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from trainer.bot.def_bot import step_calculation, valid_setting, valid_muscular, is_int_and_float
from trainer.bot.replykey_board import muscle_group, button_menu, button_start
from trainer.bot.setting import dp
from trainer.bot.states_group import ExerciseMachine
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


@dp.message(F.text == 'Создать тренажер')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(User_db, message.chat.username)
    if not is_included:
        await message.answer("Вы еще не зарегестрированны:", reply_markup=button_start())
        await state.clear()
    else:
        await message.answer('Введите название:')
        await state.set_state(ExerciseMachine.title)


@dp.message(ExerciseMachine.title)
async def set_username(message, state: FSMContext):
    is_included = await is_included_db_machine(message.text)
    if is_included:
        await message.answer("Такое название уже есть")
        await message.answer('Введите другое название:')
        await state.set_state(ExerciseMachine.title)
    else:
        await state.update_data(user_create=message.chat.username)
        await state.update_data(title=message.text)
        await message.answer(
            "Введите минимальный вес, максимальный вес, вес смены шага, шаг изменения веса 1, шаг изменения веса 2 (опцианальна):")
        await message.answer("<i>Пример с одним интервалам:\n 5, 125, 125, 5</i>", parse_mode=ParseMode.HTML)
        await message.answer("<i>Пример с двумя интервалами:\n 5, 109, 25, 5, 7 </i>", parse_mode=ParseMode.HTML)
        await state.set_state(ExerciseMachine.list_weight)


@dp.message(ExerciseMachine.list_weight)
async def set_age(message, state: FSMContext):
    if valid_setting(message.text):
        list_weight = step_calculation(message.text)
        await state.update_data(list_weight=str(list_weight), min_weight=list_weight[0], max_weight=list_weight[-1])
        await message.answer("Какая основная группа мышц:", reply_markup=muscle_group)
        await state.set_state(ExerciseMachine.group_muscles)
    else:
        await message.answer(
            "Введите минимальный вес, максимальный вес, вес смены шага, шаг изменения веса 1, шаг изменения веса 2 (опцианальна):")
        await message.answer("<i>Пример с одним интервалами: 5, 125, 125, 5</i>", parse_mode=ParseMode.HTML)
        await message.answer("<i>Пример с двумя интервалами: 5, 109, 25, 5, 7</i>", parse_mode=ParseMode.HTML)
        await state.set_state(ExerciseMachine.list_weight)


@dp.message(ExerciseMachine.group_muscles)
async def set_age(message, state: FSMContext):
    if valid_muscular(message.text):
        await state.update_data(group_muscles=message.text)
        await message.answer("Дополнительный вес:")
        await state.set_state(ExerciseMachine.add_weight)
    else:
        await message.answer("какая основная группа мышц:", reply_markup=muscle_group, )
        await state.set_state(ExerciseMachine.group_muscles)


@dp.message(ExerciseMachine.add_weight)
async def set_age(message, state: FSMContext):
    if is_int_and_float(message.text):
        await state.update_data(add_weight=message.text)
        await message.answer("Введите сколько можно добавить 1 или 2:")
        await state.set_state(ExerciseMachine.add_weight_item)
    else:
        await message.answer("Неверный вес:")
        await message.answer("Дополнительный вес:")
        await state.set_state(ExerciseMachine.add_weight)


@dp.message(ExerciseMachine.add_weight_item)
async def set_age(message, state: FSMContext):
    button_menu_ = await button_menu(message)
    if is_int_and_float(message.text):
        await state.update_data(add_weight_item=message.text)
        data = await state.get_data()
        await add_db(ExerciseMachine_db, **data)
        await message.answer(f"Регестрация прошла успешна", reply_markup=button_menu_)
        await state.clear()
    else:
        await message.answer("Введите сколько можно добавить 1 или 2:")
        await state.set_state(ExerciseMachine.add_weight_item)


"""

Конец регестрации

"""
