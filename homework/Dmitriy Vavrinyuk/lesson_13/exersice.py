import datetime
import os
import re


# Подготовка переменных пути
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
test_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
# test_path = base_path.parent.parent / 'eugene_okulik' / 'hw_13' / 'data.txt'
print(f'Путь до папке где лежит файл - {test_path}')

# Подготовка переменных времени
now = datetime.datetime.now()
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(f'Текущее время - {today_midnight}')

# Подготовка переменных
PATTERN = r"(\d{4}.\d{2}.\d{2})\s*(\d{2}.\d{1,2}.\d{1,2}.\d{6})"


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
