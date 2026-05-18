# Задание на декораторы 3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей
# числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение
import math


def calculat(func):
    def wrapper(first, second, operation):
        print('Вычисление...')
        return func(first, second, operation)
    return wrapper


@calculat
def calc(first, second, operation):
    if operation == ' ':
        if first > 0 and second > 0:
            if first == second:
                second += first
                print(second)
            elif first > second:
                second -= first
                print(second)
            elif first < second:
                first /= second
                print(first)
        elif first < 0 or second < 0:
            answer = second * first
            print(answer)
    elif operation == '+':
        print(f'Результат {first} {operation} {second} = {first + second}')
    elif operation == '-':
        print(f'Результат {first} {operation} {second} = {first - second}')
    elif operation == '*':
        print(f'Результат {first} {operation} {second} = {first * second}')
    elif operation == '/':
        print(f'Результат {first} {operation} {second} = {first / second}')
    elif operation == '**':
        hypotenuse = math.sqrt(first ** 2 + second ** 2)
        print(f'Результат теоремы Пифогора, катеты {first}, {second} и гепотенуза = {hypotenuse}')


operation = ['+', '-', '*', '/', '**', ' ']

while True:
    print('Открыт калькулятор')
    try:
        user_input_first = float(input("Введите первое число: "))
        user_input_second = float(input("Введите второе число: "))
        if isinstance(user_input_first, float) and isinstance(user_input_second, float):
            pass
        user_input_operation = input(f'Для проверки домашнего задания введите "Пробел" и нажмите кнопку "Ввод" \n'
                                     f'Для работы калькулятора введите операцию, из +, -, *, /, ** (для пифогора)\n')
        if user_input_operation in operation:
            break
    except ValueError:
        print("Ошибка! Вы ввели не число.")


calc(user_input_first, user_input_second, user_input_operation)
