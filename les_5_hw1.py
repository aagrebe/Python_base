# Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4
# отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех
# предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.

import collections


company = collections.defaultdict(list)
number = int(input('Введите количество предприятий: '))
profit = 0
for c in range(number):
    name = input(f'Введите название предприятия {c + 1}: ')
    for i in range(4):
        income = float(input(f'Введите прибыль за квартал {i + 1}: '))
        company[name].append(income)
        profit += income
print(company)

average_profit = profit / number
print(f'Средняя прибыль для всех предприятий: {average_profit} рублей')

upper_average = []
lower_average = []
for name, income in company.items():
    if sum(income) > average_profit:
        upper_average.append(name)
    elif sum(income) < average_profit:
        lower_average.append(name)

print(f'Прибыль выше среднего у кампаний: {",".join(upper_average)}')
print(f'Прибыль ниже среднего у кампаний: {",".join(lower_average)}')