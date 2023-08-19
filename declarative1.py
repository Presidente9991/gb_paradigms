"""Декларативное программирование:
Задача 3: Вычисление факториала числа. Напишите программу,
которая находит факториал заданного числа N с использованием рекурсии или встроенных функций."""
from math import factorial


def find_factorial(number):
    return factorial(number)


print(find_factorial(6))
