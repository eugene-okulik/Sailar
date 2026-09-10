# Нужно прочитать файлик, который лежит в репозитории в моей папке.
# Здесь: homework/eugene_okulik/hw_13/data.txt
#
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
# находит в нём даты и делает с этими датами то, что после них написано.
# Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер, потом дата, потом дефис и после него текст.
# У вас должен получиться код, который находит даты и для даты под номером один
# в коде должно быть реализовано то действие, которое написано в файле после этой даты.
# Ну и так далее для каждой даты.

import os
import datetime

# data_file = open('data.txt', 'r')
# data_file.read()
# print(data_file)
# data_file.close()

basedir = os.path.dirname(__file__)
files = os.listdir(basedir)
file = f'{basedir}/data.txt'
file_path = os.path.join(basedir, 'data2.txt')
file_path_2 = os.path.join(basedir, 'data2.txt')
# homework_path = os.path.dirname(os.path.dirname(file_path))

# print(basedir)
# print(files)
# print(file)
# print(file_path)
# print(homework_path)
# print(os.getcwd())

# def read_file():
#     with open(file_path, 'r') as data_file:
#         for line in data_file.readlines():
#             print(1)
#             yield line
#
# for data_line in read_file():
#     with open(file_path_2, 'a') as new_file:
#         data_line = data_line.replace('.', '').replace(',', '')
#         new_file.write(data_line)
#         # print(data_line)

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
test_path = os.path.join(homework_path, 'eugene_okulik\\Lesson_13', 'data.txt')
# test_path_2 = 'C:\\Py projects\\Sailar\\homework\\eugene_okulik\\Lesson_13\\data.txt'
print(test_path)

def read_file():
    with open(test_path, 'r') as data_file:
        for line in data_file:
            yield line

with open(test_path, 'r', encoding='utf-8') as new_file:
    print(new_file.read())

now = datetime.datetime.now()
print(now)
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)
after_midnight = now - today_midnight
print(after_midnight.seconds)
print(after_midnight)
print(now + datetime.timedelta(days=10, hours=10))