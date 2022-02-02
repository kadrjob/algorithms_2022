"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit as ti


# операции со очередью
class DeqTest:
    def __init__(self, test_list):
        self.obj = deque(test_list)

    def append(self, val):
        return self.obj.append(val)

    def pop(self):
        return self.obj.pop()

    def extend(self, val):
        return self.obj.extend(val)

    def appendleft(self, val):
        return self.obj.appendleft(val)

    def popleft(self):
        return self.obj.popleft()

    def extendleft(self, val):
        self.obj.extendleft(val)

    def get(self, idx):
        return self.obj[idx]

    def get_by_index(self, idx):
        return self.obj.index(idx)


# операции со списком
class ListTest:
    def __init__(self, test_list):
        self.obj = test_list

    def append(self, val):
        return self.obj.append(val)

    def pop(self):
        return self.obj.pop()

    def extend(self, val):
        return self.obj.extend(val)

    def appendleft(self, val):
        return self.obj.insert(0, val)

    def popleft(self):
        res = self.obj[0]
        self.obj = self.obj[1::]
        return res

    def extendleft(self, val):
        for v in val:
            self.obj.insert(0, v)
        return self.obj

    def get(self, idx):
        return self.obj[idx]

    def get_by_index(self, idx):
        return self.obj.index(idx)


def test_list1():
    print('#############################')
    print('Task1')
    print('Test LIST')
    print('Append time {}'.format(
        ti('obj.append("z")', setup='obj = ListTest(s_list)', globals=globals(), number=100000)))
    print('Pop time {}'.format(ti('obj.pop()', setup='obj = ListTest(s_list)', globals=globals(), number=100000)))
    print('Extend time {}'.format(
        ti('obj.extend("k")', setup='obj = ListTest(s_list)', globals=globals(), number=100000)))


def test_list2():
    print('#############################')
    print('Task2')
    print('Test LIST')
    print('Appendleft time {}'.format(
        ti('obj.appendleft("z")', setup='obj = ListTest(s_list)', globals=globals(), number=1000)))
    print('Popleft time {}'.format(ti('obj.popleft()', setup='obj = ListTest(s_list)', globals=globals(), number=1000)))
    print('Extendleft time {}'.format(
        ti('obj.extendleft("kmr")', setup='obj = ListTest(s_list)', globals=globals(), number=1000)))


def test_list3():
    print('#############################')
    print('Task3')
    print('Test LIST')
    print(
        'Get by index time {}'.format(ti('obj.get(4)', setup='obj = ListTest(s_list)', globals=globals(), number=1000)))
    print('Get elem by index time {}'.format(
        ti('obj.get_by_index("z")', setup='obj = ListTest(s_list)', globals=globals(), number=1000)))


def test_deque1():
    print('#############################')
    print('Task1')
    print('Test DEQUE')
    print(
        'Append time {}'.format(ti('obj.append("z")', setup='obj = DeqTest(s_list)', globals=globals(), number=100000)))
    print('Pop time {}'.format(ti('obj.pop()', setup='obj = DeqTest(s_list)', globals=globals(), number=100000)))
    print(
        'Extend time {}'.format(ti('obj.extend("k")', setup='obj = DeqTest(s_list)', globals=globals(), number=100000)))


def test_deque2():
    print('#############################')
    print('Task2')
    print('Test DEQUE')
    print('Appendleft time {}'.format(
        ti('obj.appendleft("z")', setup='obj = DeqTest(s_list)', globals=globals(), number=1000)))
    print('Popleft time {}'.format(ti('obj.popleft()', setup='obj = DeqTest(s_list)', globals=globals(), number=1000)))
    print('Extendleft time {}'.format(
        ti('obj.extendleft("kmr")', setup='obj = DeqTest(s_list)', globals=globals(), number=1000)))


def test_deque3():
    print('#############################')
    print('Task3')
    print('Test DEQUE')
    print(
        'Get by index time {}'.format(ti('obj.get(4)', setup='obj = DeqTest(s_list)', globals=globals(), number=1000)))
    print('Get elem by index time {}'.format(
        ti('obj.get_by_index("z")', setup='obj = DeqTest(s_list)', globals=globals(), number=1000)))


s_list = list("qazwsxtgtydsfsdsa")
test_list1()
test_deque1()
# print("""Результат
# Task1
# Test LIST
# Append time 0.020471711999999996
# Pop time 0.018747126999999995
# Extend time 0.025350098
# #############################
# Task1
# Test DEQUE
# Append time 0.019220955999999997
# Pop time 0.016107981000000007
# Extend time 0.023748609000000004
# """)
# print("""Вывод.
# 'Правые' операции со списком и очередью производятся примерно с одинаковой скоростью, тк нет переупорядочивания элементов списка
# """)

test_list2()
test_deque2()
# print("""Результат
# Task2
# Test LIST
# Appendleft time 0.06078079
# Popleft time 0.484284813
# Extendleft time 0.18462985499999995
# #############################
# Task2
# Test DEQUE
# Appendleft time 0.00020072700000006716
# Popleft time 0.00015804500000005106
# Extendleft time 0.0002777400000000263
#############################
# """)
# print("""Вывод.
# 'Левые' операции гораздо быстрее производятся в очереди, чем в списке т.к. в списке происходит
# постоянное переупорядочивание элементов, а очередь имеет свои оптимизированные алгоритмы для таких операций
# """)

test_list3()
test_deque3()
