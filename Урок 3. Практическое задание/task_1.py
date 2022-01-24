"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import random

from timer import Timer


##################################################################################
## СПИСОК

## O(n)
@Timer(text="Создание списка за {:.6f} секунд")
def check1_list(count=10):
    list_obj = []
    for num in range(count):
        list_obj.append(num)
    return list_obj


## O(n)
# заполнение рандомными числами
@Timer(text="Создание списка и заполнение рандомными числами за {:.6f} секунд")
def check1_list_rnd(count, rnd=100):
    list_obj = []
    for num in range(count):
        list_obj.append(random.randint(0, rnd))
    return list_obj


### O(1)
@Timer(text="Изменение списка по индексу за {:.6f} секунд")
def check2_list(list_obj, count=10):
    list_len = len(list_obj)
    for num in range(count):
        rand_int = random.randint(0, list_len)
        list_obj[rand_int] = rand_int
    return list_obj


### O(n)
@Timer(text="Изменение ОПРЕДЕЛЕННОГО ЭЛЕМЕНТА списка за {:.6f} секунд")
def check3_list(list_obj, count=10):
    list_len = len(list_obj)
    for num in range(count):
        rand_int = random.randint(0, list_len)
        res = tuple(filter(lambda x: list_obj[x] == rand_int, list_obj))
        if len(res):
            list_obj[res[0]] = rand_int


### O(n^2)
@Timer(text="Удаление ОПРЕДЕЛЕННОГО ЭЛЕМЕНТА списка за {:.6f} секунд")
def check4_list(list_obj, count=10):
    for num in range(count):
        list_len = len(list_obj)
        rand_int = random.randint(0, list_len)
        list_obj.remove(rand_int)


##################################################################################
## СЛОВАРЬ

### O(n)
@Timer(text="Создание словаря за {:.6f} секунд")
def check1_dict(count=10):
    dict_obj = {}
    for num in range(count):
        dict_obj[num] = num
    return dict_obj


### O(n)
# заполнение рандомными числами
@Timer(text="Создание словаря и заполнение рандомными числами за {:.6f} секунд")
def check1_dict_rnd(count, rnd=100):
    dict_obj = {}
    for num in range(count):
        dict_obj[random.randint(0, rnd)] = num
    return dict_obj


### O(1)
@Timer(text="Изменение словаря за {:.6f} секунд")
def check2_dict(dict_obj, count=10):
    dict_len = len(dict_obj)
    for num in range(count):
        rand_int = random.randint(0, dict_len)
        dict_obj[rand_int] = rand_int
    return dict_obj


### O(1)
@Timer(text="Удаление элемента словаря за {:.6f} секунд")
def check3_dict(dict_obj, count=10):
    dict_len = len(dict_obj)
    for num in range(count):
        rand_int = random.randint(0, dict_len)
        del dict_obj[rand_int]
    return dict_obj


# создание
lst_obj = check1_list(100000)
dict_obj = check1_dict(100000)

# создание и заполнение рандомными числами
lst_obj_rnd = check1_list_rnd(100000, 100)
dict_obj_rnd = check1_dict_rnd(100000, 100)

# изменение
check2_list(lst_obj, 100)
check3_list(lst_obj, 100)
check2_dict(dict_obj, 100)

check4_list(lst_obj, 100)
check3_dict(dict_obj, 100)