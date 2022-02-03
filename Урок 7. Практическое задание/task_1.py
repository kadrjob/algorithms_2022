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
    for i in range(0, l):
        for j in range(0, l):
            if num[j + 1] > num[j]:
                num[j + 1], num[j] = num[j], num[j + 1]
    return num


@decor
def bubble_sort_opt(num):
    l = len(num) - 1
    for i in range(0, l):
        ch_count = 0
        for j in range(0, l):
            if num[j + 1] > num[j]:
                num[j + 1], num[j] = num[j], num[j + 1]
                ch_count += 1
        if ch_count == 0:
            # print('Break')
            break
    return num


# Выполнение
if __name__ == "__main__":
    num = [randint(-100, 100) for x in range(200)]
    print(num)
    print(bubble_sort_orig(num))
    print(bubble_sort_opt(num))

"""
Результат
Оригинальный список
[-73, 75, 2, -22, -60, -40, 34, 64, 18, -62, 54, -7, 98, 56, -97, 40, -63, 53, 51, -94, -56, -91, -3, 33, 23, 86 ..]

Выполнение bubble_sort_orig заняло 0.01171875 Mib. Время выполнения 0.20621626199999998
[99, 98, 97, 97, 96, 94, 93, 93, 90, 90, 86, 85, 84, 83, 82, 82, 80, 80, 80 .. ]

Выполнение bubble_sort_opt заняло 0.0 Mib. Время выполнения 0.199874987
[99, 98, 97, 97, 96, 94, 93, 93, 90, 90, 86, 85, 84, 83, 82, 82, 80, 80, 80 .. ]

Вывод
Оптимизированная сортировка работает несколько быстрее по скорости и более оптимальная по расходу памяти
"""
