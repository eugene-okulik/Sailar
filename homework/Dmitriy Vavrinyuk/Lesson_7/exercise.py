# Задание 1 - Угадайка
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
# Подсказка: задание выполняется с помощью цикла while

import random

def Guess_the_number(number, answer):
    if answer.isdigit():
        answer = int(answer)
        while True:
            if answer == number:
                print("Yep")
                break
            elif answer > number:
                print("Too large, Try again")
            else:
                print("Too small, Try again")
            answer = input('Please enter a number: ')
            return Guess_the_number(number, answer)
    else:
        print("You typed other symbol, please enter a number and try again")
        answer = input('Please enter a number: ')
        return Guess_the_number(number, answer)

number = random.randint(1, 10)
answer = input('Please enter a number: ')

Guess_the_number(number, answer)

