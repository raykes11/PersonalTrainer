from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from trainer.data_base.def_db import all_machine, dict_user

chest_muscles = KeyboardButton(text='Грудь')
back_muscles = KeyboardButton(text='Спина')
shoulder_muscles = KeyboardButton(text='Плечи')
biceps_muscles = KeyboardButton(text='Бицепс')
triceps_muscle = KeyboardButton(text='Трицепс')
leg_muscles = KeyboardButton(text='Ноги')

muscle_group = ReplyKeyboardMarkup(keyboard=[[chest_muscles, back_muscles, shoulder_muscles],
                                             [biceps_muscles, triceps_muscle, leg_muscles]],
                                   resize_keyboard=True, one_time_keyboard=True)


def button_start():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Зарегестироватся как Пользователь')
    keyboard.button(text='Зарегестироватся как Тренер')
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)


async def button_menu(message):
    keyboard = ReplyKeyboardBuilder()
    try:
        dict_ = await dict_user(message.chat.username)
        keyboard.button(text='Начать тренировку')
    except:
        pass
    finally:
        keyboard.button(text='Создать тренажер')
        keyboard.button(text='Добавить тренажер для тренировки')
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
        keyboard.button(text='Закончить тренировку')
    else:
        for key in dict_.keys():
            keyboard.button(text=str(key))
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
