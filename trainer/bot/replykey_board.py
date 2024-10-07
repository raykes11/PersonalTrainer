from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from trainer.bot.text import user_registration_text, training_registration_text, start_training_text, \
    create_machine_text, add_machine_text, finish_training_text, chest_muscles_test, back_muscles_test, \
    shoulder_muscles_test, biceps_muscles_test, triceps_muscle_test, leg_muscles_test
from trainer.data_base.def_db import all_machine, dict_user

chest_muscles = KeyboardButton(text=f'{chest_muscles_test}')
back_muscles = KeyboardButton(text=f'{back_muscles_test}')
shoulder_muscles = KeyboardButton(text=f'{shoulder_muscles_test}')
biceps_muscles = KeyboardButton(text=f'{biceps_muscles_test}')
triceps_muscle = KeyboardButton(text=f'{triceps_muscle_test}')
leg_muscles = KeyboardButton(text=f'{leg_muscles_test}')
muscle_group = ReplyKeyboardMarkup(keyboard=[[chest_muscles, back_muscles, shoulder_muscles],
                                             [biceps_muscles, triceps_muscle, leg_muscles]],
                                   resize_keyboard=True, one_time_keyboard=True)


def button_start():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=f'{user_registration_text}')
    keyboard.button(text=f'{training_registration_text}')
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)


async def button_menu(message):
    keyboard = ReplyKeyboardBuilder()
    try:
        dict_ = await dict_user(message.chat.username)
        keyboard.button(text=f'{start_training_text}')
    except:
        pass
    finally:
        keyboard.button(text=f'{create_machine_text}')
        keyboard.button(text=f'{add_machine_text}')
        keyboard.adjust(1)
        return keyboard.as_markup(resize_keyboard=True)


async def button_spesific_muscule(muscles):
    list_ = await all_machine(muscles)
    keyboard = ReplyKeyboardBuilder()
    for name_machin in list_:
        keyboard.button(text=name_machin['title'])
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)


def button_list_weight(list_):
    keyboard = ReplyKeyboardBuilder()
    for number in list_:
        keyboard.button(text=number)
    keyboard.adjust(6)
    return keyboard.as_markup(resize_keyboard=True)


def button_number():
    keyboard = ReplyKeyboardBuilder()
    for number in range(5, 16):
        keyboard.button(text=str(number))
    keyboard.adjust(1, 4, 1, 4, 1)
    return keyboard.as_markup(resize_keyboard=True)


def button_set_trening(dict_: dict):
    keyboard = ReplyKeyboardBuilder()
    if dict_ == {}:
        keyboard.button(text=f'{finish_training_text}')
    else:
        for key in dict_.keys():
            keyboard.button(text=str(key))
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
