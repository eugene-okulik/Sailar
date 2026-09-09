# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:

import datetime
from operator import contains

time = "Jan 15, 2023 - 12:05:33"
first_date = datetime.datetime.strptime(time, '%b %d, %Y - %H:%M:%S')
print(first_date)

# 1. Распечатайте полное название месяца из этой даты
second_date = first_date.strftime('%B')
print(second_date)

# 2 Распечатайте дату в таком формате: "15.01.2023, 12:05"
third_date = first_date.strftime('%d.%m.%Y, %H:%M')
print(third_date)
