# map | filter
# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33,
# 31, 30, 32, 30, 28, 24, 23]

# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23,
                25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# Класический метод
hot_day = []
for temperature in temperatures:
    if temperature >= 28:
        hot_day.append(temperature)
hot_day.sort()
print(f'Последовательность {hot_day} \n' f'Минимальное значение {min(hot_day)}, '
      f'максимальное значение {max(hot_day)} '
      f'и среднее {sum(hot_day)/len(hot_day)}')
print('''''')


# Используя функцию filter
def compered(temperature):
    if temperature >= 28:
        return True
    else:
        return False


answer = filter(compered, temperatures)
answer2 = list(answer)
print(f'Последовательность {answer2} \n'
      f''f'Минимальное значение {min(answer2)},'
      f' максимальное значение {max(answer2)} '
      f'и среднее {sum(answer2)/len(answer2)}')
print('''''')

# Используя функцию map
# list1 = []


# def compered2(temp):
#     if temp >= 28:
#         list1.append(temp)
#     return list1
#

# total = list(map(compered2, temperatures))
# print(total)
#
# total = list(map(lambda x: x >= 28, temperatures))
# print(total)
#
# new_list = map(lambda x: x if x >= 28 else , temperatures)
# print(list(new_list))
