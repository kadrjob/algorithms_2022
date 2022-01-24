"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import sqlite3
from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4


class SqliteExecutor:

    def __init__(self):
        self.connection = sqlite3.connect('lesson3.db')

    # выполнение произвольного запроса с параметрами
    def execute_query(self, sql_text, params=[]):
        return self.connection.execute(sql_text, params).fetchall()

    def close_connection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    # инициализация таблицы с хешами
    def init_table_task2(self):
        result = self.execute_query("SELECT count(*) FROM sqlite_master WHERE type='table' and name ='task2'")
        if result[0][0] == 0:
            self.execute_query('create table task2 (id serial primary key, hash_str text, salt_str text, '
                               'user_name text)')
            self.commit()


# получение хэша
def get_hash(user_pass_str, salt_str):
    pass_obj = pbkdf2_hmac(hash_name='sha256',
                           password=user_pass_str.encode(),
                           salt=salt_str.encode(),
                           iterations=100)
    return hexlify(pass_obj).decode()


user_name = input('Введите login: ')
user_pass = input('Введите пароль: ')
user_salt = uuid4().hex
user_hash = get_hash(user_pass, user_salt)
print(f'Hash {user_hash} salt {user_salt}')

# вставка хэша и соли в БД
sql = SqliteExecutor()
sql.init_table_task2()
sql.execute_query('insert or replace into task2(user_name, hash_str,salt_str) values(?, ?, ?)',
                  [user_name, user_hash, user_salt])

# снова ввод пароля для проверки
user_name = input('Введите login: ')
user_pass = input('Введите пароль: ')

# получение из БД сохраненного хэша для данного логина
sql_res = sql.execute_query('select hash_str, salt_str from task2 where user_name=?', [user_name])
sql.close_connection()

# проверка сохраненного в БД хэша пароля
if get_hash(user_pass, sql_res[0][1]) == sql_res[0][0]:
    print('Пароли совпадают!')
else:
    print('Пароли НЕ совпадают!')
