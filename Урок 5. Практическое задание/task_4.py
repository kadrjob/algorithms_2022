"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit as ti


class TestODict:
    def __init__(self, maxsize):
        self.obj = OrderedDict({x: x ** 2 + 1 for x in range(maxsize)})

    def append(self, key, value):
        self.obj[key] = value

    def get(self, key):
        return self.obj[key]

    def pop(self, key):
        return self.obj.pop(key, 0)

    def popitem(self):
        return self.obj.popitem()

    def copy(self):
        return self.obj.copy()

    def clear(self):
        self.obj.clear()


class TestDict:
    def __init__(self, maxsize):
        self.obj = {x: x ** 2 + 1 for x in range(maxsize)}

    def append(self, key, value):
        self.obj[key] = value

    def get(self, key):
        return self.obj.pop(key, 0)

    def pop(self, key):
        return self.obj.pop(key, 0)

    def popitem(self):
        return self.obj.popitem()

    def copy(self):
        return self.obj.copy()

    def clear(self):
        self.obj.clear()


objDict = TestDict(1000)
objODict = TestODict(1000)

print('Dict append {}'.format(ti(stmt="objDict.append('zzz', 'mmm')", globals=globals(), number=10000)))
print('OrderedDict append {}'.format(ti(stmt="objODict.append('zzz', 'mmm')", globals=globals(), number=10000)))

print('Dict get {}'.format(ti(stmt="objDict.get(88)", globals=globals(), number=10000)))
print('OrderedDict get {}'.format(ti(stmt="objODict.get(88)", globals=globals(), number=10000)))

# print('Dict popitem {}'.format(ti(stmt="testObj.popitem()", setup='testObj = TestDict(1000)', globals=globals(), number=10000)))
# print('OrderedDict popitem {}'.format(ti(stmt="testObj.popitem()", setup='testObj = TestDict(1000)',globals=globals(), number=10000)))

print('Dict pop {}'.format(ti(stmt="objDict.pop(88)", globals=globals(), number=10000)))
print('OrderedDict pop {}'.format(ti(stmt="objODict.pop(88)", globals=globals(), number=10000)))

print('Dict copy {}'.format(ti(stmt="objDict.copy()", globals=globals(), number=10000)))
print('OrderedDict copy {}'.format(ti(stmt="objODict.copy()", globals=globals(), number=10000)))

print('Dict clear {}'.format(ti(stmt="objDict.clear()", globals=globals(), number=10000)))
print('OrderedDict clear {}'.format(ti(stmt="objODict.clear()", globals=globals(), number=10000)))

"""
Результаты
Dict append 0.001920054999999997
OrderedDict append 0.0020969659999999987
Dict get 0.0027263650000000014
OrderedDict get 0.001849227000000002
Dict pop 0.002875133000000002
OrderedDict pop 0.0035988640000000002
Dict copy 0.071271807
OrderedDict copy 0.906660559
Dict clear 0.0019580959999998537
OrderedDict clear 0.0020261399999998986

Выводы
Объекты практически идентичны по скорости работы
Единственно небольшие различия при копировании объектов (функция copy)
Использование OrderedDict обусловлено на уровне соглашения, что дает сторонным разработчиком понять что порядок
добавления данных в словарь имеет значение для программы 
"""
