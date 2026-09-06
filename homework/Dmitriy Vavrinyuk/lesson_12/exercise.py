# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с
# определением его стоимости. В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех
# цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина
# стебля/стоимость)(это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

# хранилище
# class Storage:
#     shared_date = {}


# Основной класс Цветы
class Flowers:
    def __init__(self, type, quantity, lifetime, price, color, length, fresh):
        self.type = type
        self.lifetime = lifetime
        self.price = price
        self.quantity = quantity
        self.color = color
        self.length = length
        self.fresh = fresh


# Подкласс Розы
class Rose(Flowers):
    def __init__(self, type, quantity, lifetime, price, color, length, fresh):
        super().__init__(type, quantity, lifetime, price, color, length, fresh)

    # def add_item(self, key, value):
    #     Storage.shared_date[key] = value
    #     # print(Storage.shared_date)

    def print_rose(self):
        print(f'Интересующий цветок сорт {self.type}, время жизни цветка {self.lifetime} и стоимость = {self.price}')


# Подкласс Дикие цветы
class Wildflowers(Flowers):
    def __init__(self, type, quantity, lifetime, price, color, length, fresh):
        super().__init__(type, quantity, lifetime, price, color, length, fresh)

    def print_Wildflowers(self):
        print(f'Интересующий цветок сорт {self.type}, время жизни цветка {self.lifetime} и стоимость = {self.price}')


# Класс букет
class Bouquet:
    def __init__(self, bouquet):
        self.bouquet = bouquet

    def print_bouquet(self):
        total_sum = 0
        count = 0
        flowers = []
        total_cost = 0

        for item in self.bouquet:
            total_sum += item.lifetime
            cost = item.price * item.quantity
            total_cost += cost
            flowers.append(item.type)
            count += 1

        avg_lifetime = round(total_sum / count)

        print(f'Общая стоимость букета: {total_cost} рублей')
        print(f'Состав букета: {", ".join(flowers)}')
        print(f'Среднее время жизни букета: {avg_lifetime} дней')
        # print(f'Стоимость букета состоит из {', '.join(flowers)} и стоять будет {total_cost}, '
        #       f'среднее время жизни букета {avg_cost}')

    # Фильтр по цвету
    def filter_by_color(self, color):
        return [flower for flower in self.bouquet if flower.color.lower() == color.lower()]

    # Фильтр по длине стебля
    def filter_by_length(self, length):
        return [flower for flower in self.bouquet if flower.length == length]

    # Фильтр по стоимости
    def filter_by_price(self, min_price=None, max_price=None):
        filtered = []

        for flower in self.bouquet:
            # Проверяем условия
            if min_price is not None and flower.price < min_price:
                continue
            if max_price is not None and flower.price > max_price:
                continue
            filtered.append(flower)
        return filtered

    # Фильтр по свежести
    def filter_by_fresh(self, fresh):
        return [flower for flower in self.bouquet if flower.fresh == fresh]

    # Универсальный метод фильтрации
    def filter_bouquet(self, filter_type, value=None, min_price=None, max_price=None):
        if filter_type == 'color':
            return self.filter_by_color(value)
        elif filter_type == 'length':
            return self.filter_by_length(value)
        elif filter_type == 'price':
            return self.filter_by_price(min_price, max_price)
        elif filter_type == 'fresh':
            return self.filter_by_fresh(value)
        else:
            print("Ошибка: filter_type должен быть 'color', 'length' или 'price'")
            return []

        # Метод для вывода информации отфильтрованных цветов
    def print_filtered_flowers(self, filter_type, value=None, min_price=None, max_price=None):
        if filter_type == 'price':
            filtered = self.filter_by_price(min_price, max_price)
            if min_price is not None and max_price is not None:
                print(f"\nЦветы с ценой от {min_price} до {max_price} рублей:")
            elif min_price is not None:
                print(f"\nЦветы с ценой от {min_price} рублей:")
            elif max_price is not None:
                print(f"\nЦветы с ценой до {max_price} рублей:")
        else:
            filtered = self.filter_bouquet(filter_type, value)
            if filter_type == 'color':
                print(f"\nЦвет цветов - {value}:")
            elif filter_type == 'fresh':
                replacements = {True: "да", False: "нет"}
                print(f"\nСвежие цветы - {replacements[value]}:")
            else:
                print(f"\nДлина цветов - {value}:")

        if not filtered:
            print("Цветы не найдены")
            return

        for flower in filtered:
            print(f"  - {flower.type}: {flower.quantity} шт., цена {flower.price} руб., "
                  f"длина стебля {flower.length} см, цвет {flower.color}")

        # Подсчет общей стоимости отфильтрованных цветов
        total_filtered_cost = sum(flower.price * flower.quantity for flower in filtered)
        total_filtered_quantity = sum(flower.quantity for flower in filtered)
        print(f"Общая стоимость отфильтрованных цветов: {total_filtered_cost} рублей, в "
              f"количестве {total_filtered_quantity}")

    # # Фильтр, по параметрам свежесть, цвет, длина стебля, стоимости
    # def filter_bouquet(self, filter_type, value):
    #
    #     filtered_flowers = []
    #
    #     for item in self.bouquet:
    #         if filter_type == 'color':
    #             if item.color.lower() == value.lower():  # Игнорируем регистр
    #                 filtered_flowers.append(item)
    #         elif filter_type == 'length':
    #             if item.length == value:
    #                 filtered_flowers.append(item)
    #         elif filter_type == 'lifetime':
    #             if item.lifetime == value:
    #                 filtered_flowers.append(item)
    #         elif filter_type == 'price':
    #             if item.price >= value:
    #                 filtered_flowers.append(item)
    #         else:
    #             print("Ошибка: выбранный параметр должен быть 'color', 'length', 'lifetime' или 'price'")
    #             return []
    #
    #     return filtered_flowers
    #
    # # ВЫВОДА ОТФИЛЬТРОВАННОЙ ИНФОРМАЦИИ (Цвет)
    # def print_filtered_flowers(self, filter_type, value):
    #
    #     filtered = self.filter_bouquet(filter_type, value)
    #
    #     if not filtered:
    #         print(f"Цветы с {filter_type} = {value} не найдены")
    #         return
    #
    #     print(f"\nНайдены цветы с {filter_type} = {value}:")
    #     for flower in filtered:
    #         print(f"  - {flower.type}: {flower.quantity} шт., цена {flower.price} руб., "
    #               f"длина стебля {flower.length} см, цвет {flower.color}")
    #
    #     # Подсчет общей стоимости отфильтрованных цветов
    #     total_filtered_cost = sum(flower.price * flower.quantity for flower in filtered)
    #     print(f"Общая стоимость отфильтрованных цветов: {total_filtered_cost} рублей")


flower_1 = Rose('Пинк Флойд роза', 5, 2, 350, 'Красный', 30, True)
flower_2 = Rose('Чайная роза', 6, 6, 250, 'Оранжевый', 30, True)
flower_3 = Rose('Кустовая роза', 8, 5, 200, 'Красный', 30, False)

flower_4 = Wildflowers('Василек', 10, 10, 125, 'Синий', 15, True)
flower_5 = Wildflowers('Ромашка', 15, 12, 100, 'Белый', 15, False)
flower_6 = Wildflowers('Лилия', 1, 5, 350, 'Белый', 15, True)

# flower_1.add_item('Пинк Флойд', 3)
# flower_2.add_item('Чайная', 6)
# flower_3.add_item('Кустовая', 8)

list_flowers = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6]

# Выводим весь букет
# print(Storage.shared_date)
# a = Bouquet(list_flowers)
# a.print_bouquet()
#
# # Фильтруем по цвету
# print("\n" + "="*50)
# a.print_filtered_flowers('color', 'Красный')
#
# # Фильтруем по длине стебля
# print("\n" + "="*50)
# a.print_filtered_flowers('length', 30)
#
# # Фильтруем по другому цвету
# print("\n" + "="*50)
# a.print_filtered_flowers('color', 'Белый')
#
# print("\n" + "="*50)
# a.print_filtered_flowers('price', '200')
# print("\n" + "="*50)


# Создаем букет
list_flowers = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6]
a = Bouquet(list_flowers)

# Выводим весь букет
a.print_bouquet()

# Фильтр по цвету
print("\n" + "=" * 50)
a.print_filtered_flowers('color', 'Красный')

# Фильтр по длине
print("\n" + "=" * 50)
a.print_filtered_flowers('length', 30)

# Фильтр по стоимости (от 200 до 300 рублей)
print("\n" + "=" * 50)
a.print_filtered_flowers('price', min_price=200, max_price=300)

# Фильтр по стоимости (дороже 250 рублей)
print("\n" + "=" * 50)
a.print_filtered_flowers('price', min_price=250)

# Фильтр по стоимости (дешевле 200 рублей)
print("\n" + "=" * 50)
a.print_filtered_flowers('price', max_price=200)

# Фильтр по свежести
print("\n" + "=" * 50)
a.print_filtered_flowers('fresh', True)
