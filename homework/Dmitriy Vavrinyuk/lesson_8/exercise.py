# Задание 1
# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный
# бонус.
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

from random import random, randint

# Переменные задаются один раз и генератор вовзрващет 1 раз измененое значение


# def assist(salary, bonus):
#     if bonus == True:
#         salary += int(randint(1, 100))
#     yield salary, bonus
#
#
# salary = int(input("Enter your start salary: "))
# bonus = bool(randint(0, 1))
#
# for x in assist(salary, bonus, 5):
#     print((f" {salary}, {x[1]} - $'{x[0]}'"))

# Переменные задаются в теле генератора и вращаются в цикле столько раз пока выполняется условие


def assist(limit=10):
    cont = 1
    total = 0
    while cont <= limit:
        cont += 1
        bonus = bool(randint(0, 1))
        salary = int(input("Enter your salary: "))
        if bonus is True:
            total = salary + int(randint(1, 100))
        yield salary, bonus, total


for x in assist(5):
    print((f" {x[0]}, {x[1]} - $'{x[2]}'"))
