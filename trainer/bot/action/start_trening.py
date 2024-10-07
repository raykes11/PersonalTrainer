from aiogram import F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from trainer.bot.replykey_board import button_set_trening, button_start, button_menu
from trainer.bot.setting import dp
from trainer.bot.states_group import StartTrening
from trainer.bot.text import start_training_text, already_not_registered, choice_machine, request_add_machine_text, \
    finish_training_complited_text, reped
from trainer.data_base.def_db import dict_user, is_included_db
from trainer.moduls.user_db import User_db

'''
Начало тренировки:

class StartTrening(StatesGroup):
    user = State()
    set_exercise = State()
    history_weight = State()
    history_calories = State()
    date_last_training = State()
    history_date = State()
    history_machine = State()
    list_sleep_time = State()
'''


@dp.message(F.text == f'{start_training_text}')
async def sing_up(message, state: FSMContext):
    is_included = await is_included_db(User_db, message.chat.username)
    if not is_included:
        await message.answer(f"{already_not_registered}", reply_markup=button_start())
        await state.clear()
    else:
        try:
            dict_ = await dict_user(message.chat.username)
            await state.update_data(user=dict_)
            await state.update_data(set_exercise=dict_['set_exercise'])
            await message.answer(f'{choice_machine} {str(dict_['set_exercise'].keys())}',
                                 reply_markup=button_set_trening(dict_['set_exercise']), parse_mode=ParseMode.HTML)
            await state.set_state(StartTrening.set_exercise)
        except:
            button_menu_ = await button_menu(message)
            await message.answer(f'{request_add_machine_text}', reply_markup=button_menu_)


@dp.message(StartTrening.set_exercise)
async def set_age(message, state: FSMContext):
    dict_ = await state.get_data()
    if dict_['set_exercise'] == {}:
        button_menu_ = await button_menu(message)
        await message.answer(f'{finish_training_complited_text}', reply_markup=button_menu_)
        await state.clear()
    else:
        iter_ = dict_['set_exercise'].pop(message.text)
        await message.answer(f'''{message.text}
                                Первый подход вес: {iter_[0][0]} {reped} {iter_[1][0]}
                                Второй подход вес: {iter_[0][1]} {reped} {iter_[1][1]}
                                Третий подход вес: {iter_[0][2]} {reped} {iter_[1][2]}
                                ''', reply_markup=button_set_trening(dict_['set_exercise']), parse_mode=ParseMode.HTML)
        await state.update_data(set_exercise=dict_['set_exercise'])
        await state.update_data(group_muscles=message.text)
        await state.set_state(StartTrening.set_exercise)
