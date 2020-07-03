from random import randint

sum = 0

try:
    with open("text_5.txt", "w+", encoding="utf-8") as file:
        for el in range(randint(3, 15)):
            file.write(str(randint(1, 21)) + " ")

        file.seek(0)
        summList = list(file.read().split(" "))
        for num in summList:
            try:
                sum += int(num)
            except ValueError:
                continue
        print(f"Сумма чисел = {sum}")

except IOError:
    print("Error!")
