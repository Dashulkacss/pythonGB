class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num < 0:
            return "Разница количества ячеек меньше нуля"
        else:
            return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        try:
            return round(self.num / other.num)
        except:
            return "Делить на нуль нельзя"

    def make_order(self, dig):
        i = 0
        line = ""
        while i < self.num:
            for el in range(dig):
                i += 1
                line += "*"
                if i == self.num:
                    return line
            line += "\n"
        return line


cell1 = Cell(56)
cell2 = Cell(12)
print(f"Сумма: {cell1 + cell2}")
print(f"Разница: {cell1 - cell2}")
print(f"Новая клетка, умноженная: {cell1 * cell2}")
print(f"Новая клетка, деленная: {cell1 / cell2}")
print(cell2.make_order(4))
