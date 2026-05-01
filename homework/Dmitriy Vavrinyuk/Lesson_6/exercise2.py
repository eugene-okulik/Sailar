# Задание 2
# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz". Для чисел которые кратны одновременно и 3 и 5
# надо печатать "FuzzBuzz". Иначе печатать число.

numb_sequences = []
for numb in range(1, 101):
    if numb % 5 == 0 and numb % 3 == 0:
        numb = "FuzzBuzz"
    elif numb % 3 == 0:
        numb = "Fuzz"
    elif numb % 5 == 0:
        numb = "Buzz"

    # if numb % 3 == 0:
    #     if numb % 5 == 0:
    #         numb = "FuzzBuzz"
    #         print(numb)
    #     numb = "Fuzz"
    # elif numb % 5 == 0:
    #     numb = "Buzz"
    print(numb)
