my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for el in my_list if (el > my_list[my_list.index(el) - 1] and my_list.index(el) != 0)]
print(new_list)

more_than = [my_list[num] for num in range(1,len(my_list)) if my_list[num]>my_list[num-1]]