"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
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
def bubble_sort_orig(num):
    l = len(num) - 1
    for i in range(l, 0, -1):
        for j in range(l, 0, -1):
            if num[j] < num[j-1]:
                num[j-1], num[j] = num[j], num[j-1]
    return num

num = [randint(-100,100) for x in range(200)]
print(num)
print(bubble_sort_orig(num))