'''
step_calculation(string) - Калькулятор шага увеличения массы
from_str_in_list(string) -  Перевод из строки в список, если список сохранен в виде строки
is_int_and_float(string) - Проверка является ли строка числом
valid_setting(string) - Проверяет правельно ли введены насстройки расчета шага увеличения веса
valid_muscular(string) - Проверяет в строке есть ли упоменание нужной группы мышц
'''
from trainer.bot.text import chest_muscles_test, back_muscles_test, shoulder_muscles_test, biceps_muscles_test, \
    triceps_muscle_test, leg_muscles_test


def step_calculation(string):
    list_weight = []
    text = string.split(',')
    number = [int(a) for a in text]
    min_weight = number[0]
    max_weight = number[1]
    step_weight = number[2]
    iter_list = number[3:]
    weight = min_weight
    while step_weight > weight:
        list_weight.append(weight)
        weight += iter_list[0]
    while max_weight > weight:
        list_weight.append(weight)
        weight += iter_list[1]
    list_weight.append(max_weight)
    return list_weight


def from_str_in_list(string):
    string = string.replace("[", "").replace("]", "").split(',')
    return string


def is_int_and_float(string):
    float_ = string.replace(",", ".")
    try:
        float_ = float(float_)
        return True
    except ValueError:
        return False


def valid_setting(string):
    try:
        list_ = step_calculation(string)
        return True
    except:
        return


def valid_muscular(string):
    chest_muscles = [f"{chest_muscles_test}", f"{back_muscles_test}", f"{shoulder_muscles_test}",
                     f"{biceps_muscles_test}", f"{triceps_muscle_test}", f"{leg_muscles_test}"]
    if string in chest_muscles:
        return True
    else:
        return False

# print(valid_muscular("Грудь"))
# valid_setting('5,25,15,5')
# print(step_calculation('5,25,25,5'))
# is_int_and_float('12')
# step_calculation('5, 109, 25, 5,7')
# print(from_str_in_list('[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]'))
