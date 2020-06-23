from math import factorial


def fact(el):
    my_list = range(1, el + 1)
    for i in my_list:
        #       print(" Test", i , " Return ", i*i)
        yield factorial(i)


n = 4
for el in fact(n):
    print("факториал ", el)
