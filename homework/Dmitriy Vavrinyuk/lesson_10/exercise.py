# Задание на декораторы 1
# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished" после выполнения
# декорированной функции.

# Код, использующий этот декоратор может выглядеть, например, так:

# @finish_me
# def example(text):
#     print(text)

# example('print me')

# В результате работы будет такое:
# print me
# finished

def universal_function(func):
    def wrapper():
        print('print me')
        result = func()
        return result
    return wrapper


@universal_function
def func1():
    print('finished')


func1()
