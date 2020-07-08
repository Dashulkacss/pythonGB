class MyOwnZeroEx(Exception):
    def __init__(self, txt = "Делить на нуль нельзя!"):
        self.txt = txt

    def __str__(self):
        return self.txt


num = 100
data = input(f"На что будем делить {num}? ")

try:
    if int(data) == 0:
        raise MyOwnZeroEx()
    res = num / int(data)
except MyOwnZeroEx as err:
    print(err)
except ValueError:
    print("Чиселки вводи, да")
else:
    print(res)