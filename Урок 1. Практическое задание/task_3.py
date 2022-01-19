"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

# O(n)
def check_1(dict_obj):
    v = None

    for item in dict_obj.items():
        if v is None:
            v = item
        else:
            if item[1] > v[1]:
                v = item
    return v

# O(N log N)
def check_2(dict_obj):
    lst_obj = list(dict_obj.items())
    lst_obj.sort(key=lambda i: i[1], reverse=True)

    return lst_obj[:3]

# O(N^2)
def check_3(dict_obj):
    sorted_values = sorted(dict_obj.values(), reverse=True)
    sorted_dict = {}

    f = 1
    for i in sorted_values:
        for k in dict_obj.keys():
            if dict_obj[k] == i:
                sorted_dict[k] = dict_obj[k]
                if f == 3:
                    return sorted_dict
                f += 1

    return sorted_dict


company_lst = {"A": 1500, "B": 2000, "C": 3000, "D": 4000, "F": 500}

print(check_1(company_lst))
print(check_2(company_lst))
print(check_3(company_lst))
