"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from random import randint
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

from functools import lru_cache


@lru_cache(maxsize=1000)
def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse1(number // 10)}'


print('Оптимизированная декоратором lru_cache функция recursive_reverse1')
print(
    timeit(
        'recursive_reverse1(num_100)',
        setup='from __main__ import recursive_reverse1, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse1(num_1000)',
        setup='from __main__ import recursive_reverse1, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse1(num_10000)',
        setup='from __main__ import recursive_reverse1, num_10000',
        number=10000))

print('Вывод. В данном случае, считаю что мемоизация уместна, тк \n'
      'прирост скорости очевиден на всех диапазонах вычислений.\n'
      'Также можно использовать декоратор из встроенной библиотеки.\n'
      'При его использовании наблюдается еще большее ускорение вычисления.\n'
      'Хотя, следуя теории данные все время разные и кешем ни разу не пользуемся \n'
      'Считаю, что тут замеры в помощь, если есть прирост скорости почему не использовать')

"""
Результаты
Не оптимизированная функция recursive_reverse
0.03201319
0.037100314999999995
0.074500945
Оптимизированная функция recursive_reverse_mem
0.002536448999999996
0.0025942850000000017
0.0037049290000000235
Оптимизированная декоратором lru_cache функция recursive_reverse1
0.001053735
0.0008223900000000062
0.0009470310000000148
Вывод. В данном случае, считаю что мемоизация уместна, тк 
прирост скорости очевиден на всех диапазонах вычислений.
Также можно использовать декоратор из встроенной библиотеки.
При его использовании наблюдается еще большее ускорение вычисления.
Хотя, следуя теории данные все время разные и кешем ни разу не пользуемся 
Считаю, что тут замеры в помощь, если есть прирост скорости почему не использовать

Process finished with exit code 0


"""