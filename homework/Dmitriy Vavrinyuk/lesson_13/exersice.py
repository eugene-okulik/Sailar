# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt

# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл, находит в нём даты и
# делает с этими датами то, что после них написано. Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер, потом дата, потом дефис и после него текст. У вас должен получиться код,
# который находит даты и для даты под номером один в коде должно быть реализовано то действие, которое написано
# в файле после этой даты. Ну и так далее для каждой даты.

import datetime
import os
import re


# Подготовка переменных пути
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
test_path = os.path.join(homework_path, 'eugene_okulik\\hw_13', 'data.txt')
# test_path_2 = 'C:\\Py projects\\Sailar\\homework\\eugene_okulik\\Lesson_13\\data.txt'
print(f'Путь до папке где лежит файл - {test_path}')

# Подготовка переменных времени
now = datetime.datetime.now()
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(f'Текущее время - {today_midnight}')

# Подготовка переменных
PATTERN = r"(\d{4}.\d{2}.\d{2})\s*(\d{2}.\d{1,2}.\d{1,2}.\d{6})"

# Поиск и чтение файла по строчкл
def read_file():
    with open(test_path, 'r') as data_file:
        for line in data_file:
            yield line

#  Открытие файла по строчное сравнение по условию
with open(test_path, 'r', encoding='utf-8') as new_file:
    for line in new_file:
        match = re.search(PATTERN, line)
        # print(line)
        if '1.' in line:
            if match:
                raw = match.group()  # '2023-11-27 20:34:13.212967'
                dc = datetime.datetime.strptime(raw, "%Y-%m-%d %H:%M:%S.%f")
                print(dc + datetime.timedelta(days=7))
                # print(dc)
        elif '2.' in line:
            if match:
                raw = match.group()
                dc = datetime.datetime.strptime(raw, "%Y-%m-%d %H:%M:%S.%f")
                dc = dc.strftime("%A")
                print(dc)
        elif '3.' in line:
            if match:
                raw = match.group()
                dc = datetime.datetime.strptime(raw, "%Y-%m-%d %H:%M:%S.%f")
                sub = now - dc
                print(sub.days)

# print(now)
# today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
# print(today_midnight)
# after_midnight = now - today_midnight
# print(after_midnight.seconds)
# print(after_midnight)
