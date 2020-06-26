from itertools import count, cycle
from sys import argv

"""итератор, повторяющий элементы некоторого списка, определенного заранее"""


def abra(my_list, iterations):
    i = 0
    iter = cycle(my_list)
    while i < int(iterations):
        print(next(iter))
        i += 1


NameScript, Number, iterations = argv

print("Name script: ", NameScript)
print("Number: ", Number)
print("Iterations: ", iterations)

"""Итератор, генерирующий целые числа, начиная от указанного"""
for el in count(int(Number)):
    if el > (int(Number) + 10):
        break
    else:
        print(el)
print()
abra("abra",iterations)
