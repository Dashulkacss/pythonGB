def my_func(a, b, c):
    """Возвращает сумму наибольших значений"""
    return a + b + c - min(a, b, c)


a = 1
b = 2
c = 3
print(my_func(int(input("a = ")),int(input("b = ")), int(input("c = "))))
