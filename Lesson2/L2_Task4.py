my_str = input("Введите строку ")
index = 0
new_str = my_str.split(" ")

while index < len(new_str):
    print(index+1, new_str[index] if len(new_str[index])<11 else new_str[index][:10])
    index +=1

