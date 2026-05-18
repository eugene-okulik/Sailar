# Создаём библиотеку
# Первый класс
# Создайте класс book с атрибутами:
#
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:

# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована

# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага

# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


class Book:
    def __init__(self, page_material, text, book_tite, author, num_pages, ISBN, reserved):
        self.page_material = page_material
        self.text = text
        self.book_tite = book_tite
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = reserved


class Textbooks(Book):
    def __init__(self, page_material, text, book_tite, author, num_pages, ISBN, reserved, school_subject,
                 school_class, exercise):
        super().__init__(page_material, text, book_tite, author, num_pages, ISBN, reserved)
        self.school_subject = school_subject
        self.school_class = school_class
        self.exercise = exercise


book_1 = Book('Бумага', 'Да', 'Идиот', 'Достоевский', 500,
              '123-5-45-7456123', True)
book_2 = Book('Картон', 'Нет', 'Война и мир', 'Толстой', 3500,
              '123-5-45-7456124', False)
book_3 = Book('Папирус', 'Да', 'Мастер и маргарита', 'Булгаков', 1920,
              '123-5-45-7456345', False)
book_4 = Book('Береста', 'Нет', 'Мертые души', 'Гоголь', 1200,
              '123-5-45-7454513', True)
book_5 = Book('Пергамент', 'Да', 'Геройнашего времени', 'Лермантов', 1690,
              '123-5-45-7754151', False)


book_6 = Textbooks('Бумага', 'Да', 'Алгебра', 'Автор 1', 1690,
              '123-5-45-7754151', False, 'Математика', '6 класс', True )
book_7 = Textbooks('Бумага', 'Да', 'Физика', 'Автор 2', 1200,
              '123-5-45-7754151', True, 'Физика', '9 класс', True)
book_8 = Textbooks('Бумага', 'Да', 'ИЗО', 'Автор 3', 3500,
              '123-5-45-7754151', False, 'Рисование', '3 класс', False)


# library = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8]
library1 = [book_1, book_2, book_3, book_4, book_5]
library2 = [book_6, book_7, book_8]


# def print(book):
#     for item in library1:
#         if item.school_subject is not None:
#             if item.reserved is True:
#                 print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                       f'материал: {item.page_material}, зарезервирована')
#             else:
#                 print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                       f'материал: {item.page_material}')
#         else:
#             if item.reserved is True:
#                 print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                       f'предмет {item.school_subject}, класс: {item.school_class}, зарезервирована')
#             else:
#                 print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                       f'предмет {item.school_subject}, класс: {item.school_class}')


def print_book(book):
    for item in library1:
        if item.reserved is True:
            print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
                  f'материал: {item.page_material}, зарезервирована')
        else:
            print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
                  f'материал: {item.page_material}')


def print_textbooks(book):
    print('\n')
    for item in library2:
        if item.reserved is True:
            print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
                  f'предмет {item.school_subject}, класс: {item.school_class}, зарезервирована')
        else:
            print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
                  f'предмет {item.school_subject}, класс: {item.school_class}')


# print(library)
print_book(library1)
print_textbooks(library2)

# print(f'Назвние: {book_8.book_tite}, Автор: {book_8.author}, страниц: {book_8.num_pages}, '
#                       f'предмет {book_8.school_subject}, класс: {book_8.school_class}')