# Задание на декораторы 2
# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
# @repeat_me
# def example(text):
#     print(text)
# example('print me', count=2)
#
# В результате работы будет такое:
#
# print me
# print me
#
# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор,
# который сможет обработать такой код:
# @repeat_me(count=2)
# def example(text):
#     print(text)
# example('print me')
import functools


def universal_function(func):
    def wrapper(*args):
        wrapper.count += 1
        counter = wrapper.count
        print(f'Function {func.__name__}, started')
        print(f'Function {func.__name__}, repeat - {counter}')
        return func(*args)
    wrapper.count = 0
    return wrapper


@universal_function
def function_2(text):
    print(f'Function {text} \n')


function_2("finished")
function_2("finished")
function_2("finished")

def repeat(n):
    def decorator(func):
        print(f'Function {func.__name__} repeat')
        def wrapper(*args):
            for x in range(n):
                func(*args)
        return wrapper
    return decorator


@repeat(3)
def example(text):
    print(text)


example('print me')
