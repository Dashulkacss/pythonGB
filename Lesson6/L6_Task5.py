class Stationery:
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        return print("Начинаем создавать шедевры с помощью ручки")


class Pencil(Stationery):

    def draw(self):
        return print("Я смотрю ты любишь черкать... Чёрно-белый мир")


class Handle(Stationery):
    def draw(self):
        return print("Я смотрю ты уверен в своих силах.. Погнали, у тебя только 1 шанс")

pen1 = Pen("Офисная ручка Золотишко")
pen2 = Pen("Офисная ручка Оболтус")
pencil1 = Pencil("Чёрный карандаш Союз")
handle1 = Handle("Маркер чёрный Какой-то")

pen1.draw()
pencil1.draw()
handle1.draw()

