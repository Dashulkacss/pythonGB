my_list = [7, 5, 3, 3, 2]
num = 3
index = len(my_list) - 1
print(my_list)

if num > my_list[0]:
    my_list.insert(0, num)
else:
    while index > 0:
        print(num," " ,my_list[index])
        if num <= my_list[index]:
            my_list.insert(index + 1, num)
            break
        else:
            index -= 1

print(my_list)
