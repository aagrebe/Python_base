# Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число 
# представляется как коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их 
# как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’,
# ‘9’, ‘F’, ‘E’]. 

from collections import deque

numbers = [str(_) for _ in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
print(numbers)

first_number = deque(input('Введите первое число в шестнадцатеричной системе: ').upper())
second_number = deque(input('Введите второе число в шестнадцатеричной системе: ').upper())

if len(first_number) > len(second_number):
    first_number, second_number = second_number, first_number

print(f'Первое число: {"".join(list(first_number))}')
print(f'Второе число : {"".join(list(second_number))}')

second_number.reverse()
result = deque()
k = 0
j = -1
for i in second_number:
    one = numbers.index(i)
    two = numbers.index(first_number[j])
    result.appendleft(numbers[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
    j -= 1
    if j == -len(first_number) - 1:
        break

diff = len(second_number) - len(first_number)
second_number.reverse()
for i in range(diff):
    result.appendleft(second_number[i])
if k == 1:
    result.appendleft('1')
print(f'Результат сложения двух чисел: {"".join(list(result))}')