# Задание на List comprehension
# Дан такой кусок прайс листа:
#
# (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)
import re

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# print(PRICE_LIST)
# new_price = PRICE_LIST.split('\n')
# new_price = re.split(r' |\n', PRICE_LIST)
# print(new_price)

new_dict = (dict(item.split(' ') for item in PRICE_LIST.split('\n')))
# new_dict1 = {item: value(re.sub('р', '', value)) for item, value in new_dict.items()}
new_dict2 = {item: int(value.replace('р', '')) for item, value in new_dict.items()}

print(new_dict)
# print(new_dict1)
print(new_dict2)


# empty_dict = {}
# for k, v in new_dict.items():
#     v = re.sub('р', '', v)
#     number = int(v)
#     empty_dict[k] = number
# print(empty_dict)
#
# asd = {k: v for k, v is (v(re.sub('р', '', v))) in new_dict.items()}
# asd = {}
# print(asd)
