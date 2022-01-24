"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib

from timer import Timer


def get_hash(user_str):
    return hashlib.md5(user_str.encode('utf-8')).hexdigest()


@Timer(text="Поиск подстрок за {:.6f} секунд")
def unique_substr(stri):
    n = len(stri)
    res = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            res1 = stri[i:j]
            if res1 != stri:
                res.add(get_hash(res1))
    return len(res)


user_str = input('Введите строку: ')
##print(all_substr(user_str))
print(f'{user_str} - {unique_substr(user_str)} уникальных подстрок')
