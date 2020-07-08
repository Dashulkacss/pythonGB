from typing import List


class IsDigitEx(Exception):
    def __init__(self, txt="Non digit!"):
        self.txt = txt

    def __str__(self):
        return self.txt

    @staticmethod
    def check_digit(line):
        for el in line:
            if not el.isdigit():
                return False
        return True



res = []
print("Введите числа. Когда надоест пиши stop")
while True:
    data = input().split()
    if data[0] == "stop":
        break
    try:
        if IsDigitEx.check_digit(data):
            res.extend(list(map(int, data)))
        else:
            raise IsDigitEx()

    except IsDigitEx as DE:
        print(DE)

print(res)

