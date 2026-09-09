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
    def __init__(self, type, lifetime, price, color, length, fresh):
        self.type = type
        self.lifetime = lifetime
        self.price = price
        self.color = color
        self.length = length
        self.fresh = fresh


# Подкласс Розы
class Rose(Flowers):
    def __init__(self, type, lifetime, price, color, length, fresh):
        super().__init__(type, lifetime, price, color, length, fresh)

    # def add_item(self, key, value):
    #     Storage.shared_date[key] = value
    #     # print(Storage.shared_date)

    def print_rose(self):
        print(f'Интересующий цветок сорт {self.type}, время жизни цветка {self.lifetime} и стоимость = {self.price}')


# Подкласс Дикие цветы
class Wildflowers(Flowers):
    def __init__(self, type, lifetime, price, color, length, fresh):
        super().__init__(type, lifetime, price, color, length, fresh)

    def print_Wildflowers(self):
        print(f'Интересующий цветок сорт {self.type}, время жизни цветка {self.lifetime} и стоимость = {self.price}')


# Класс букет
class Bouquet:
    def __init__(self, bouquet):
        self.bouquet = bouquet
        self._calc_bouquet()

    def _calc_bouquet(self):
        self.flowers = []
        self.count = 0
        self.total_cost = 0
        self.total_lifetime = 0
        self.total_sum = 0

        for item in self.bouquet:
            cost = item.price
            self.total_cost += cost
            self.flowers.append(item.type)
            self.count += 1
            self.total_sum += item.lifetime

        self.avg_lifetime = round(self.total_sum / self.count)

    def print_bouquet(self):
        print(f'Количество цветов {self.count} шт')
        print(f'Общая стоимость букета: {self.total_cost} рублей')
        print(f'Состав букета: {", ".join(self.flowers)}')
        return self.flowers, self.total_cost, self.count, self.total_sum

    def lifetime_bouquet(self):
        print("\n" + "=" * 50)
        print(f'Cреднее время жизни букета {self.avg_lifetime}')

    # Общая сортировка
    def sort_flowers(self, key, value):
        # Определяем направление сортировки
        reverse_sort = (value == 'Убывание')

        # Сортируем по нужному ключу
        if key == 'price':
            sort_list = sorted(self.bouquet, key=lambda x: x.price, reverse=reverse_sort)
        elif key == 'lifetime':
            sort_list = sorted(self.bouquet, key=lambda x: x.lifetime, reverse=reverse_sort)
        else:
            print("Неизвестный ключ сортировки")
            return

        # Выводим результаты
        print(f"Сортировка по {key} ({value}):")
        for i, flower in enumerate(sort_list, 1):
            print(f"{i}. {flower.type} - цена: {flower.price}, жизнь: {flower.lifetime} дней")

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
        count = 0
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
            count += 1
            # print(flower)
            print(f"  - {flower.type}: цена {flower.price} руб., "
                  f"длина стебля {flower.length} см, цвет {flower.color}")

        # Подсчет общей стоимости отфильтрованных цветов
        total_filtered_cost = sum(flower.price for flower in filtered)
        print(f"Общая стоимость отфильтрованных цветов: {total_filtered_cost} рублей, в "
              f"количестве {count}")


flower_1 = Rose('Пинк Флойд роза', 2, 450, 'Красный', 30, True)
flower_2 = Rose('Чайная роза', 6, 350, 'Оранжевый', 30, True)
flower_3 = Rose('Кустовая роза', 5, 200, 'Красный', 30, False)
flower_4 = Wildflowers('Василек', 10, 125, 'Синий', 15, True)
flower_5 = Wildflowers('Ромашка', 12, 100, 'Белый', 15, False)
flower_6 = Wildflowers('Лилия', 5, 600, 'Белый', 15, True)
flower_7 = Wildflowers('Тюльпан', 13, 475, 'Белый', 15, False)
flower_8 = Wildflowers('Гортезия', 4, 1200, 'Белый', 30, True)

# Создаем букет
list_flowers = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6, flower_7, flower_8]
a = Bouquet(list_flowers)

# Выводим весь букет
a.print_bouquet()
a.lifetime_bouquet()

# Выводим сортировку по цене
print("\n" + "=" * 50)
a.sort_flowers('price', 'Убывание')
print("\n" + "=" * 50)
a.sort_flowers('price', 'Возрастание')

# Выводим сортировку по сроку жизни
print("\n" + "=" * 50)
a.sort_flowers('lifetime', 'Убывание')

# Фильтр по цвету
print("\n" + "=" * 50)
a.print_filtered_flowers('color', 'Красный')

print("\n" + "=" * 50)
a.print_filtered_flowers('color', 'Белый')

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
