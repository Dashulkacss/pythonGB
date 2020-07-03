"""" Начальные """


# class Transport:
#
#     # Конструктор, атрибуты объекта
#     def __init__(self, auto_name, auto_model, auto_year=2018):
#         self.auto_name = auto_name
#         self._auto_model = auto_model
#         self.__auto_year = auto_year
#         print(f"Model {self._auto_model}. Year - {self.__auto_year}")
#         self.on_start()
#         # Auto.auto_count += 1
#
#     # Методы
#     def on_start(self, speed=10):
#         print(f"Go-go car {self.auto_name} with {speed}!")
#
#     def on_stop(self):
#         print("Stop.")
#
#
# class Auto(Transport):
#     def __init__(self, auto_name, auto_model, auto_year, pas):
#         super().__init__(auto_name, auto_model, auto_year)
#         self.pas = pas
#
#     def one(self):
#         print("One")
#
#
# auto1 = Auto("Lexus", "CX2", "2020", "5")
# auto1.one()


# car_1 = Auto("Mazda", "CX", 2019)
# car_2 = Auto("Mazda", "CX5", 2019)
# car_3 = Auto("Mazda", "CX9", 2019)
# car_4 = Auto("Mazda", "CX", 2020)
# print(car_4._auto_model)
# print(car_4._Auto__auto_year)

class Transport:
    def transport_method(self):
        print("Родитель транспорт")


class Auto(Transport):
    def auto_method(self):
        print("дочерний от авто")


class Bus(Transport):
    def bus_method(self):
        print("дочерний бас транспорт")


a = Auto()
a.auto_method()
b = Bus()
b.transport_method()
t = Transport()
