"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import defaultdict
from functools import reduce


# через ООП
class HexClass:
    def reduce_func(self, x, y):
        return str(x).upper() + str(y).upper()

    def __init__(self, str_hex):
        self.str_hex = str_hex.upper()
        self.my_list = list(self.str_hex)

    def __str__(self):
        return self.str_hex

    def __add__(self, other):
        return list(str(hex(
            int(reduce(self.reduce_func, self.my_list), 16) + int(reduce(self.reduce_func, other.my_list),
                                                                  16))).upper()[2::])

    def __mul__(self, other):
        return list(str(hex(
            int(reduce(self.reduce_func, self.my_list), 16) * int(reduce(self.reduce_func, other.my_list),
                                                                  16))).upper()[2::])


# через defaultdict
def use_default_dict(a, b):
    def reduce_func(x, y):
        return str(x).upper() + str(y).upper()

    my_x = defaultdict().fromkeys(a)
    my_y = defaultdict().fromkeys(b)

    return (list(str(hex(int(reduce(reduce_func, my_x), 16) + int(reduce(reduce_func, my_y), 16))).upper()[2::]),
            list(str(hex(int(reduce(reduce_func, my_x), 16) * int(reduce(reduce_func, my_y), 16))).upper()[2::])
            )


a1 = HexClass('A2')
a2 = HexClass('C4F')
print(f'Введены числа {a1} и {a2}')
print(f'Сумма чисел {a1 + a2}')
print(f'Произведение чисел {a1 * a2}')
# print("""
# Результат
# Используя ООП
# Введены числа A2 и C4F
# Сумма чисел ['C', 'F', '1']
# Произведение чисел ['7', 'C', '9', 'F', 'E']
# """)

res = use_default_dict('A2', 'C4F')
print(f"""
Используя defaultdict 
Сумма чисел {res[0]} 
Произведение чисел {res[1]}""")
# print("""
# Результат
# Используя defaultdict
# Сумма чисел ['C', 'F', '1']
# Произведение чисел ['7', 'C', '9', 'F', 'E']
# """)
