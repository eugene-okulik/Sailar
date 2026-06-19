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
    page_material = 'Бумага'
    text = 'Да'
    def __init__(self, type, book_tite, author, num_pages, ISBN, reserved=True):
        self.book_tite = book_tite
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = reserved
        self.type = type


class Textbooks(Book):
    def __init__(self, type, book_tite, author, num_pages, ISBN, school_subject='', school_class='', exercise=''):
        super().__init__(type, book_tite, author, num_pages, ISBN, reserved=True)
        self.school_subject = school_subject
        self.school_class = school_class
        self.exercise = exercise

# Книги
book_1 = Book(False, 'Идиот', 'Достоевский', 500, '123-5-45-7456123', )
book_2 = Book(False, 'Война и мир', 'Толстой', 3500, '123-5-45-7456124')
book_3 = Book(False, 'Мастер и маргарита', 'Булгаков', 1920, '123-5-45-7456345')
book_4 = Book(False, 'Мертые души', 'Гоголь', 1200, '123-5-45-7454513')
book_5 = Book(False, 'Геройнашего времени', 'Лермантов', 1690, '123-5-45-7754151')

# Учебники
book_6 = Textbooks(True, 'Алгебра', 'Автор 1', 1690, '123-5-45-7754151',
                   'Математика', '6 класс', True)
book_7 = Textbooks(True, 'Физика', 'Автор 2', 1200, '123-5-45-7754151',
                   'Физика', '9 класс', True)
book_8 = Textbooks(True, 'ИЗО', 'Автор 3', 3500, '123-5-45-7754151',
                   'Рисование', '3 класс', False)

book_1.reserved = True
book_2.reserved = True
book_3.reserved = False
book_4.reserved = True
book_5.reserved = False
book_6.reserved = True
book_7.reserved = False
book_8.reserved = False

# library1 = [book_1, book_2, book_3, book_4, book_5]
# library2 = [book_6, book_7, book_8]
# full_library = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8]


def print_book_all(book):
    if book.type is False:
        if book.reserved is True:
            print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
                  f'материал: {book.page_material}, зарезервирована')
        else:
            print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
                  f'материал: {book.page_material}')
    else:
        if book.reserved is True:
            print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
                  f'предмет {book.school_subject}, класс: {book.school_class}, зарезервирована')
        else:
            print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
                  f'предмет {book.school_subject}, класс: {book.school_class}')


# def print_book(book):
#     if book.reserved is True:
#         print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
#               f'материал: {book.page_material}, зарезервирована')
#     else:
#         print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
#               f'материал: {book.page_material}')


# def print_textbook(book):
#     print('\n')
#     if book.reserved is True:
#         print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
#               f'предмет {book.school_subject}, класс: {book.school_class}, зарезервирована')
#     else:
#         print(f'Назвние: {book.book_tite}, Автор: {book.author}, страниц: {book.num_pages}, '
#               f'предмет {book.school_subject}, класс: {book.school_class}')


# def print_books(book):
#     print('\n')
#     for item in library1:
#         if item.reserved is True:
#             print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                   f'материал: {item.page_material}, зарезервирована')
#         else:
#             print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                   f'материал: {item.page_material}')


# def print_textbooks(book):
#     print('\n')
#     for item in library2:
#         if item.reserved is True:
#             print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                   f'предмет {item.school_subject}, класс: {item.school_class}, зарезервирована')
#         else:
#             print(f'Назвние: {item.book_tite}, Автор: {item.author}, страниц: {item.num_pages}, '
#                   f'предмет {item.school_subject}, класс: {item.school_class}')

# унифицрованная фунция фильтрующая данные по пармету Type
print_book_all(book_1)
print_book_all(book_2)
print_book_all(book_3)
print_book_all(book_4)
print_book_all(book_5)
print_book_all(book_6)
print_book_all(book_7)
print_book_all(book_8)

# для вызова функции под конкретный тип литерутуры
# print_book(book_1)
# print_book(book_2)
# print_book(book_3)
# print_book(book_4)
# print_book(book_5)
# print_textbook(book_6)
# print_textbook(book_7)
# print_textbook(book_8)

# Для работы с списками
# print_books(library1)
# print_textbooks(library2)
# print_books(full_library)
