# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


# Задание 2

list_1 = "результат операции: 42"
list_2 = "результат операции: 514"
list_3 = "результат работы программы: 9"

lists = (list_1, list_2, list_3)
result = int()

# string_index = list_1.index(": ")
# value_int = int(list_1[string_index + 1: ]) + 10
# result += value_int
# print(result)

for item in lists:
    string_index = item.index(": ")
    value_int = int(item[string_index + 1: ]) + 10
    result += value_int
print(result)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print("Students", (", ".join(students)), "study these subjects:", (", ".join(subjects)))

students = ", ".join(students)
subjects = ", ".join(subjects)

my_text = 'Students {0} study these subjects: {1}'
print(my_text.format(students, subjects))

my_text = f"Students {students} study these subjects: {subjects}"
print(my_text)
