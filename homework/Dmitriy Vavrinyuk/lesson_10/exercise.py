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

def universal_function():
    def func1():
        return func1
        print('Hello world')
    # print('Function universal_function')


@universal_function
def func1():
    print('Function func1')

func1()
