from functools import reduce


def my_func(a, b):
    return a * b


my_list = [el for el in range(100, 1001, 2)]
print(reduce(my_func, my_list))

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))