"""
2. Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся пользователем с
клавиатуры
"""


def foo():
    num = 1
    while True:
        yield num
        num += 1
        if num == 4:
            num = 1


n = int(input("Введите n: "))
obj = foo()

for i in range(n):
    print(next(obj), end='-')