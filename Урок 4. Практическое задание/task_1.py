"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# фильтрация элементов списка по условию
# время обработки списка возрастает
def func_2(nums):
    new_arr = list(filter(lambda x: x % 2 == 0, nums))
    return new_arr


# сразу получаем элемент списка а не по его индексу как в func_1
# время обработки списка возрастает
def func_3(nums):
    new_arr = []
    for x in nums:
        if int(x) % 2 == 0:
            new_arr.append(nums.index(x))

    return new_arr


# используем list comprehension
# время обработки списка возрастает
def func_4(nums):
    new_arr = [nums.index(x) for x in nums if x % 2 == 0]
    return new_arr


# формируем массив обходя перечисление (индекс, значение)
# на маленьких массивах скорость работы аналогична с func_1
# на больших массивах самый быстрый алгоритм
def func_5(nums):
    return [idx for idx, val in enumerate(nums) if val % 2 == 0]


# nums = list(range(200))
nums = [1, 3, 1, 3, 7, 4, 5, 1]

print(func_1(nums))
print(func_2(nums))
print(func_3(nums))
print(func_4(nums))
print(func_5(nums))

print(timeit(stmt='func_1(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_2(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_3(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_4(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_5(nums)', globals=globals(), number=1000))


"""
Результат
[5]
[4]
[5]
[5]
[5]
0.0011956970000000008
0.0015646739999999985
0.001801278
0.0011004369999999992
0.0011428090000000016
"""