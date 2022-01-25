"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from random import randint
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]
array = []
for i in range(1000):
    array.append(randint(1, 10))


# самый быстрый линейный алгоритм (для небольших массивов с повторяющимися числами)
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# самый быстрый линейный алгоритм (для БОЛЬШИХ массивов с повторяющимися числами)
# за счет того что, уменьшается длина подсчитываемых элементов в массиве
# (в нашем случае array.count(m_l) будет вызвана всего 10 раз)
# по сравнению с func_1 в которой она будет вызвана len(array) раз
def func_3():
    m_l = max(set(array), key=lambda x: array.count(x))
    return f'Самое часто встречающееся число {m_l} встречается в массиве {array.count(m_l)}'


print(func_1())
print(func_2())
print(func_3())

# pr = profile.Profile()
# pr.enable()
# print(func_3())
# print(func_1())
# pr.disable()
# pr.dump_stats('task4.pstat')
# pr.print_stats()

print(timeit(stmt='func_1()', globals=globals(), number=1000))
print(timeit(stmt='func_2()', globals=globals(), number=1000))
print(timeit(stmt='func_3()', globals=globals(), number=1000))

"""
Результаты
Чаще всего встречается число 5, оно появилось в массиве 122 раз(а)
Чаще всего встречается число 5, оно появилось в массиве 122 раз(а)
Самое часто встречающееся число 5 встречается в массиве 122
"""