def my_func(x, y):
    print(x ** y)


def my_func_strange_way(x, y):
    result = 1 / x
    y += 1
    while y != 0:
        result *= 1 / x
        y += 1
    print(result)


x = int(input("введите положительное x "))
y = int(input("введите отрицательное y "))
my_func(x, y)
my_func_strange_way(x, y)
