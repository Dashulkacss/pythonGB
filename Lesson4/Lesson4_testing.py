# import Lesson4.ModuleTest as p

# p.sh_ms()
# print(p.calc())
# _______________________________
"""Скрипты"""
# from sys import argv

# script_name, first_p, second_p, third_p = argv

# print("Name script: ", script_name)
# print("first_p script: ", first_p)
# print("second_p script: ", second_p)
# print("third_p script: ", third_p)

"""Генераторы"""
# my_list = [1, 2, 3, 4, 5, 6]
# new_list = [el + 10 for el in my_list if el % 2 == 0]
# print(new_list)

# new_= {el**2 for el in range(11)}
# print(new_)

# new_dict= {el: el **2 for el in range(11)}
# print(new_dict)

# new_1 = (el**2 for el in range(5))
# print(list(new_1))

# for i in new_1:
#    print(i)

"""Random"""

# from random import randint, randrange, random

# print(randint(0,10))
# print(randrange(10, 20, 2))
# print(random() * 100)

"""Yield"""

# def gen():
#    for el in (10, 20, 30):
#       yield el


# for i in gen():
#    print(i)

# print(next(gen()))

"""Functools"""
# from functools import reduce

# def my_func(prev_el, el):
#    return prev_el + el

# print(reduce(my_func, [10,20,30]))

#from itertools import count, cycle

#for el in count(7):
 #   if el > 15:
  #      break
 #   else:
 #       print(el)

#c = 0
#for el in cycle("ABC"):
#    if c > 10:
 #       break
#    else:
#        print(el)
 #       c +=1

