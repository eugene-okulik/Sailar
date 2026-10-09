import mysql.connector as mysql

# Подключение к БД
mydb = mysql.connect(
    user="st-onl",
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    database="st-onl",
    port=25060,
)

# -- Вывод инфомрации для проверки
cursor = mydb.cursor(dictionary=True)
# print("\n" + "=" * 50)

# --  Создайте студента (student)
cursor.execute("insert into students (name, second_name) values ('Alina', 'Fedorova')")
student_id = cursor.lastrowid
print(student_id)
# mydb.commit()

cursor.execute(f"select * from students where id = {student_id}")
print_cursor = cursor.fetchall()
print(print_cursor)

# -- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
cursor.executemany("insert into books (title, taken_by_student_id) values (%s, %s)",
                   [('Покемоноведение', student_id), ('Спирицизм', student_id)])
# mydb.commit()

# Проверка
cursor.execute("select * from books where taken_by_student_id = %s", (student_id,))
print_cursor = cursor.fetchall()
print(print_cursor)

# -- Создайте группу (group) и определите своего студента туда
cursor.execute("insert into `groups` (title, start_date, end_date) values (%s, %s, %s)",
               ('Магический питон2', 'oct 2026', 'nov 2026',))
group_id = cursor.lastrowid
cursor.execute("update `students` set group_id = %s where id = %s",
               (group_id, student_id))
# mydb.commit()

cursor.execute("select * from `groups` where id = %s", (group_id,))
print_cursor = cursor.fetchall()
print(print_cursor)

cursor.execute(f"select * from students where id = {student_id}")
print_cursor = cursor.fetchall()
print(print_cursor)

# -- Создайте несколько учебных предметов (subjects)
cursor.execute("insert into subjects (title) values (%s)", ('Покемология',))
sub1 = cursor.lastrowid

cursor.execute("insert into subjects (title) values (%s)", ('Окультизм',))
sub2 = cursor.lastrowid

# lessons = ['Урок как приручить покемона', 'Кормление покемонов', 'Начертание рун', 'Чтение заклятий']
# print(lessons[0])

# cursor.executemany("insert into lessons (title, subject_id) values (%s, %s)",
#                    [
#     (lessons[0], sub1),
#     (lessons[1], sub1),
#     (lessons[2], sub2),
#     (lessons[3], sub2),
# ])

# cursor.execute("insert into lessons (title, subject_id) values (%s, %s)", (lessons[0], sub1))
# les1 = cursor.lastrowid
# cursor.execute("insert into lessons (title, subject_id) values (%s, %s)", (lessons[1], sub1))
# les2 = cursor.lastrowid
# cursor.execute("insert into lessons (title, subject_id) values (%s, %s)", (lessons[2], sub2))
# les3 = cursor.lastrowid
# cursor.execute("insert into lessons (title, subject_id) values (%s, %s)", (lessons[3], sub2))
# les4 = cursor.lastrowid

lessons_data = [('Урок как приручить покемона', sub1),
                ('Кормление покемонов',         sub1),
                ('Начертание рун',              sub2),
                ('Чтение заклятий',             sub2),
                ]

lesson_ids = {}
for title, sub_id in lessons_data:
    cursor.execute(
        "insert into lessons (title, subject_id) values (%s, %s)",
        (title, sub_id)
    )
    lesson_ids[title] = cursor.lastrowid
print(lesson_ids)
# mydb.commit()

cursor.execute("select * from lessons order by id desc limit 10")
print_cursor = cursor.fetchall()
print(print_cursor)

# -- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
cursor.executemany("insert into marks (value, lesson_id, student_id) values (%s, %s, %s)",
                   [
                       (4, lesson_ids['Урок как приручить покемона'], student_id),
                       (3, lesson_ids['Кормление покемонов'], student_id),
                       (5, lesson_ids['Начертание рун'], student_id),
                       (4, lesson_ids['Чтение заклятий'], student_id),
                   ])

cursor.execute("select * from marks order by id desc limit 10")
print_cursor = cursor.fetchall()
print(print_cursor)

# --  Все оценки студента
cursor.execute("select s.name, s.second_name, s.group_id, m.value "
               "from students s "
               "join marks m on s.id = m.student_id "
               "where s.id = %s "
               "order by m.id desc limit 10",
               (student_id,))
print_cursor = cursor.fetchall()
print(print_cursor)

# -- Все книги, которые находятся у студента
cursor.execute("select s.name, s.second_name, s.group_id, b.title "
               "from students s "
               "join books b "
               "on s.id = b.taken_by_student_id "
               "where s.id = %s",
               (student_id,))
print_cursor = cursor.fetchall()
print(print_cursor)

cursor.execute("""
               select s.name,
                      s.second_name,
                      g.title   as group_title,
                      b.title   as book_title,
                      sub.title as subject_title,
                      l.title   as lesson_title,
                      m.value   as mark_value
               from students s
                        left join `groups` g on g.id = s.group_id
                        left join `books` b on b.taken_by_student_id = s.id
                        left join `marks` m on m.student_id = s.id
                        left join `lessons` l on l.id = m.lesson_id
                        left join `subjects` sub on sub.id = l.subject_id
               where s.id = %s
               order by l.title, b.title
               """, (student_id,))
# print(cursor.fetchall())

rows = cursor.fetchall()
print("получено строк:", len(rows))
for r in rows:
    print(r)

cursor.close()
mydb.close()
