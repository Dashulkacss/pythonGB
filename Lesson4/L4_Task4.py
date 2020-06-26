from random import randint
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

r_list = [randint(-10, 10) for i in range(20)]
print(r_list)
uniq_list = [el for el in r_list if r_list.count(el) == 1]
print(uniq_list)