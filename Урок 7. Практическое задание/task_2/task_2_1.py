"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import time
from random import randint

from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_end = time.perf_counter() - time_start
        print(f"Выполнение {func.__name__} заняло {mem_diff} Mib. Время выполнения {time_end}")
        return res

    return wrapper


@decor
def gnome_sort(m):
    num = [randint(1, 50) for x in range(1, 2 * m + 2)]

    i, l_num = 1, len(num)
    while i < l_num:
        if num[i - 1] <= num[i]:
            i += 1
        else:
            num[i - 1], num[i] = num[i], num[i - 1]
            if i > 1:
                i -= 1
    return num[m]


@decor
def gnome_sort_opt(m):
    num = [randint(1, 50) for x in range(1, 2 * m + 2)]

    i, j, l_num = 1, 2, len(num)
    while i < l_num:
        if num[i - 1] <= num[i]:
            i, j = j, j + 1
        else:
            num[i - 1], num[i] = num[i], num[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return num[m]


# Выполнение
if __name__ == "__main__":
    print('Гномья сортировка')
    print(gnome_sort(10))
    print(gnome_sort(100))
    print(gnome_sort(1000))

    print('Гномья сортировка (Оптимизированная)')
    print(gnome_sort_opt(10))
    print(gnome_sort_opt(100))
    print(gnome_sort_opt(1000))

"""
Результаты
Гномья сортировка
Выполнение gnome_sort заняло 0.01171875 Mib. Время выполнения 0.200097611
32
Выполнение gnome_sort заняло 0.0 Mib. Время выполнения 0.20811433199999996
25
Выполнение gnome_sort заняло 0.0 Mib. Время выполнения 0.8548153829999999
26
Гномья сортировка (Оптимизированная)
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.19993121499999988
28
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.20395070999999998
23
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.6339803829999999
25

"""