"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from statistics import median
import time
from memory_profiler import memory_usage
from random import randint

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
def test_func(m):
    num = [randint(1, 50) for x in range(1, 2 * m + 2)]
    return median(num)

print(test_func(10))