"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def run(val, att):
    """
    :param val: значение
    :param att: порядковый номер попытки
    :return:
    """
    if att == 0:
        return 0

    return (1 if att % 2 == 0 else -1) * val + run(val / 2, att - 1)


att_count = input('Введите количество элементов: ')
if not att_count.isdigit():
    print('Вы ввели не число')
else:
    res = run(1, int(att_count))
    print(f'Количество элементов {int(att_count)} их сумма {res}')
