# Задание 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))
a = number // 100
b = (number - a * 100) // 10
c = number - a * 100 - b * 10
sum_number = a + b + c
multiply_number = a * b * c
print(f'Сумма чисел трехзначного числа: {sum_number}')
print(f'Произведение чисел трехзначного числа: {multiply_number}')