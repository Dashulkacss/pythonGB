my_list = [12, False, "jump", 23.1, True, "fun", "ololo"]
index = 0

while index < len(my_list) - 1:
    n = my_list[index]
    my_list[index] = my_list[index + 1]
    my_list[index + 1] = n
    index += 2

print(my_list)
