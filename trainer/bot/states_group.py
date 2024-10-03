from aiogram.fsm.state import StatesGroup, State


class RegistrationState(StatesGroup):
    nickname = State()
    first_name = State()
    age = State()
    height = State()
    weight = State()
    average_calories = State()
    sleep_time = State()
    password = State()


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


class ExerciseMachine(StatesGroup):
    user_create = State()
    title = State()
    max_weight = State()
    min_weight = State()
    add_weight = State()
    add_weight_item = State()
    list_weight = State()
    group_muscles = State()


class SpecificationExerciseMachine(StatesGroup):
    nickname = State()
    title = State()
    specification = State()


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


class StartTrening(StatesGroup):
    user = State()
    set_exercise = State()
    history_weight = State()
    history_calories = State()
    date_last_training = State()
    history_date = State()
    history_machine = State()
    list_sleep_time = State()
