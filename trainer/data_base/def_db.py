from sqlalchemy import text, select, insert, update, delete

from trainer.bot.def_bot import from_str_in_list
from trainer.data_base.db import engine
from trainer.moduls.base import Base
from trainer.moduls.exercise_machine_db import ExerciseMachine_db
from trainer.moduls.user_machine import UserMachine_db
from trainer.moduls.trainers_db import Trainer_db
from trainer.moduls.user_db import User_db

"""

connect_bd(): Проверка подключения к базе данных
init_models(): Создание таблиц
get_db(table): Запрос всей информации из баззы дынных. table = Названию classa в файлах папки модуль
get_db_where_nickname(table, nickname): Запрос всей информации из баззы дынных конкретного пользователя. table = Trainer_db или User_db
get_db_where_title(title): Запрос на конкретный тренажер. В виде списка classa UserMachine_db, title = назвие тренажера
get_all_machine_where_group_muscles(group_muscles):Запрос всей информации из баззы дынных конкретной машины, для конкретной группы мышц . classa UserMachine_db
add_db(table, **kwargs): Добавление в базу данных нового пользователя
update_db(table, nickname, **kwargs): Изменение пользователя в базу данных
delet_db(table, nickname): Удаление пользователя из бызы данных
is_included_db(table, nickname): Есть ли пользователь в базе данных
is_included_db_machine(title): Есть ли Тренажер в базе данных
all_machine(group_muscles): вспомогательная функция, получить все тренажеры в виде списка из словорей
get_db_machine_where_title(title): Вспомогательнаая функция. Запрос на конкретный тренажер. В виде словоря classa UserMachine_db, title = назвие тренажера
set_trening(nickname, kwargs): Добовление тренажера в set_exercise  
dict_user(nickname): Вся информация о юзере в виде словоря

"""
async def connect_bd():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res=}")


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db(table):
    stmt = select(table)
    answer_db = []
    async with engine.connect() as session:
        query_set = await session.execute(stmt)
        answer_db.extend([a for a in query_set])
    return answer_db


async def get_db_where_nickname(table, nickname):
    stmt = select(table).where(table.nickname == nickname)
    answer_db = []
    async with engine.connect() as session:
        query_set = await session.execute(stmt)
        answer_db.extend([a for a in query_set])
    return answer_db


async def get_db_where_title(title):
    stmt = select(ExerciseMachine_db).where(ExerciseMachine_db.title == title)
    answer_db = []
    async with engine.connect() as session:
        query_set = await session.execute(stmt)
        answer_db.extend([a for a in query_set])
    return answer_db


async def get_all_machine_where_group_muscles(group_muscles):
    stmt = select(ExerciseMachine_db).where(ExerciseMachine_db.group_muscles == group_muscles)
    answer_db = []
    async with engine.connect() as session:
        query_set = await session.execute(stmt)
        answer_db.extend([a for a in query_set])
    return answer_db


async def add_db(table, **kwargs):
    async with engine.connect() as session:
        id = await session.execute(text(F'SELECT COUNT (id) FROM {table.__tablename__}'))
        id = id.first()[0]
        kwargs['id'] = id + 1
        query_set = await session.execute(
            insert(table), [kwargs, ])
        await session.commit()


async def update_db(table, nickname, **kwargs):
    async with engine.connect() as session:
        query_set = await session.execute(update(table).where(table.nickname == nickname).values(kwargs))
        await session.commit()


async def delet_db(table, nickname):
    async with engine.connect() as session:
        query_set = await session.execute(delete(table).where(table.nickname == nickname))
        await session.commit()


async def is_included_db(table, nickname):
    user = await get_db_where_nickname(table, nickname)
    if user == []:
        return False
    else:
        return True


async def is_included_db_machine(title):
    user = await get_db_where_title(title)
    if user == []:
        return False
    else:
        return True

async def all_machine(group_muscles):
    list_ = await get_all_machine_where_group_muscles(group_muscles)
    all_machine_on_group_muscles = []
    for machine in list_:
        dict_ = {}
        dict_['title'] = machine[1]
        dict_['add_weight'] = machine[5]
        dict_['add_weight_item'] = machine[6]
        dict_['list_weight'] = machine[7]
        dict_['group_muscles'] = machine[8]
        dict_['user_create'] = machine[9]
        copy_dict = dict_.copy()
        all_machine_on_group_muscles.append(copy_dict)
    return all_machine_on_group_muscles


async def get_db_machine_where_title(title):
    machine = await get_db_where_title(title)
    dict_ = {}
    dict_['title'] = machine[0][1]
    dict_['add_weight'] = machine[0][5]
    dict_['add_weight_item'] = machine[0][6]
    dict_['list_weight'] = from_str_in_list(machine[0][7])
    dict_['group_muscles'] = machine[0][8]
    dict_['user_create'] = machine[0][9]
    return dict_


async def set_trening(nickname, kwargs):
    old_data = await get_db_where_nickname(User_db, nickname)
    data = {}
    if old_data[0][14] == None:
        data['set_exercise'] = str(kwargs)
        await update_db(User_db, nickname, **data)
    else:
        dict_ = eval(old_data[0][14])
        new_data = {**dict_, **kwargs}
        data['set_exercise'] = str(new_data)
        await update_db(User_db, nickname, **data)


async def dict_user(nickname):
    list_ = await get_db_where_nickname(User_db, nickname)
    dict_ = {}
    dict_["id"] = list_[0][0]
    dict_["nickname"] = list_[0][1]
    dict_["first_name"] = list_[0][2]
    dict_["age"] = list_[0][3]
    dict_["height"] = list_[0][4]
    dict_["weight"] = list_[0][5]
    dict_["history_weight"] = list_[0][6]
    dict_["history_calories"] = list_[0][7]
    dict_["average_calories"] = list_[0][8]
    dict_["date_last_training"] = list_[0][9]
    dict_["history_date"] = list_[0][10]
    dict_["machine"] = list_[0][11]
    dict_["history_machine"] = list_[0][12]
    dict_["sleep_time"] = list_[0][13]
    # dict_ ["list_sleep_time"] = list_[0]
    dict_["set_exercise"] = eval(list_[0][14])
    dict_["last_set_exercise"] = list_[0][15]
    dict_["password"] = list_[0][16]
    dict_["status"] = list_[0][17]
    dict_["trainer"] = list_[0][18]
    return dict_

# print(asyncio.run(set_trening('raykes11')))
# print(asyncio.run(dict_user('raykes11')))
# print(asyncio.run(get_db_where_nickname(User_db,'raykes11')))
