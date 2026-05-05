# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
#
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

import sys
sys.set_int_max_str_digits(100000)


def num_fibanacci():
    num1, num2 = 0, 1
    # sum = 0
    while True:
        # yield sum
        # sum = num1 + num2
        # num1 = num2
        # num2 = sum

        yield num2
        num1, num2 = num2, num1 + num2


count = 1
for number in num_fibanacci():
    # print(number)
    if count == 5:
        print(f' Распечатка несколько значений, пятое число {number}')
    elif count == 200:
        print(f' Распечатка несколько значений, двухсотое число {number}')
    elif count == 1000:
        print(f' Распечатка несколько значений, тысячное число {number}')
    elif count == 100000:
        print(f' Распечатка несколько значений, стотысячное число {number}')
        break
    count += 1

