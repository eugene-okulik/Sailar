# Добавление
# insert into students values (1, "Ivan", "Ivanov", 1)
# insert into `groups` (title, start date, end date) values ('test', 'Oct', 'Dec')

# выбор
# select * from students
# select * from students where id = 2 - равно
# select * from students where id <> 2 - не равно
# select * from students where second_name = 'ivanov' and  name = 'Ivan' - условие и
# select * from students where second_name = 'ivanov' or  name = 'Ivan' -  условие или
# select * from students order by id desc limit 3 - такая конструкция вывести с конца
# select * from students order by id asc limit 3 - такая конструкция вывести с начала
# select * from students order by id desc limit 2, 1 - такой конструкцией миы указывает сколько пропустить и вывести

# замена
# update students set name = 'Dmitriy' where id = 2 - обновление конкретного поля для id = 2

# Удаление
# delete from students where id = 12

# inner Join
# select * from students join books on students.id = books.taken by students_id

# left join - берем данные всей левой таблицы и соответствия с правой
# select * from students left join books on students.id = books.taken by students_id

# right join - берем данные всей правой таблицы и соответствия с левой
# select * from students right join books on students.id = books.taken by students_id

# full outer join - в mySQL не поддерживает данную функцию
# select * from students full outer join books on students.id = books.taken by students_id


# select s.name, s.second_name, b.title
# from student s
# left join books b
# on s.id = b.taken by s
# where b.title = 'Java

# Создайте студента (student)
# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
# Создайте группу (group) и определите своего студента туда
# Создайте несколько учебных предметов (subjects)
# Создайте по два занятия для каждого предмета (lessons)
# Поставьте своему студенту оценки (marks) для всех созданных вами занятий


# Все действия нужно выполнить именно в том порядке, который указан здесь в задании.
#
# Получите информацию из базы данных:
#
# Все оценки студента
# Все книги, которые находятся у студента
# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
# Все запросы, которые сделаете, сохраняйте в файлик с расширением .txt или .sql, и сдавайте как обычно
