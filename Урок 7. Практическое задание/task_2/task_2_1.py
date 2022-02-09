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
    return num


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
    return num


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
Выполнение gnome_sort заняло 0.01171875 Mib. Время выполнения 0.19918026599999997
[2, 3, 6, 9, 10, 10, 13, 22, 23, 24, 27, 31, 32, 36, 38, 40, 40, 41, 46, 47, 49]
Выполнение gnome_sort заняло 0.0 Mib. Время выполнения 0.205895198
[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, ..]
Выполнение gnome_sort заняло 0.015625 Mib. Время выполнения 0.8259462169999999
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...]
Гномья сортировка (Оптимизированная)
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.19994389499999987
[1, 1, 3, 8, 9, 9, 11, 12, 18, 19, 19, 22, 24, 26, 28, 30, 30, 32, 35, 44, 45]
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.20390679
[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, ...]
Выполнение gnome_sort_opt заняло 0.0 Mib. Время выполнения 0.6289519929999998
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
"""