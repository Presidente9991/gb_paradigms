""" Императивное программирование:
Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных
чисел в диапазоне от 1 до заданного числа N. """


def summ_even(number):
    summ = 0
    for item in range(1, number + 1):
        if item % 2 == 0:
            summ += item

    return summ


user_number = int(input('Input number: '))
print(summ_even(user_number))
