import json


class Stock:
    def __init__(self):
        self.stock_dict = {}

    def new_to_stock(self, item):
        self.stock_dict.update({item.name: item.count})

    def move_to_another_department(self, name, count):
        if self.stock_dict[name] == count:
            del self.stock_dict[name]
        else:
            self.stock_dict[name] = self.stock_dict[name] - count

    def __str__(self):
        return json.dumps(self.stock_dict, indent=4, sort_keys=True)


class OfficeEquipment:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Printer(OfficeEquipment):
    def __init__(self, name, count, isColor):
        super().__init__(name, count)
        self.isColor = isColor


class Scanner(OfficeEquipment):
    def __init__(self, name, count, speed):
        super().__init__(name, count)
        self.speed = speed


class Xerox(OfficeEquipment):
    def __init__(self, name, count, height):
        super().__init__(name, count)
        self.height = height


stock = Stock()
xer1 = Xerox("Xerox V3", 3, 2)
pri1 = Printer("Printer Canon", 10, True)
stock.new_to_stock(xer1)
stock.new_to_stock(pri1)

print(stock)
stock.move_to_another_department("Xerox V3", 1)
print("-"*10)
print(stock)

