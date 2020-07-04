"""Переопределение стандарнтных методов"""

# class Auto:
#
#     def __init__(self, p1):
#         self.p1 = p1
#         # self.p2 = p2
#
#     # def __del__(self):
#     #     print("Delete object!")
#     def __str__(self):
#         # return f"{self.p1} and {self.p2}"
#         return f"{self.p1}"
#
#     def __call__(self, new_p1):
#         self.p1 = new_p1
#
#     # def __add__(self, other):
#     #     return Auto(self.p1 + other.p1, self.p2 + other.p2)


# auto1 = Auto(23, 45)
# auto2 = Auto(33, 55)
# auto3 = Auto(73, 63)
# del auto1
# print(auto1 + auto2)

"""Call"""
# auto1 = Auto(23)
# auto2 = Auto(33)
# print(auto1, auto2)
# auto1("one")
# auto2("two")
# print(auto1, auto2)


"""Новое значение - setattr """
# class MyClass:
#     pass
#     # def __setattr__(self, key, value):
#     #     self.__dict__[key] = value
#     #     print(self.__dict__)
#
#
# m1 = MyClass()
# m1.name = "J"
# m1.surname = "N"
# print(m1.__dict__)

"""Less Then"""

# class Salary:
#     val = 50000
#
#     def __lt__(self, other):
#         print("Salary less?")
#         return self.val < other.val
#
#
# class Prize:
#     val = 15000
#
#     def __lt__(self, other):
#         print("Prize less?")
#         return self.val < other.val
#
#
# s1 = Salary()
# p1 = Prize()
# # print(s1.val < p1.val)
# print(s1 < p1)
# print(p1 < s1)

"""NEXT PART interface"""

# from abc import ABC, abstractclassmethod
#
#
# class MyAbcCL(ABC):
#     @abstractclassmethod
#     def m1(self):
#         pass
#
#     @abstractclassmethod
#     def m2(self):
#         pass
#
#
# class MyClass(MyAbcCL):
#     def m1(self):
#         pass
#
#     def m2(self):
#         pass
#
#
# my1 = MyClass()

"""Декоратор"""

# class MyClass:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#
#     @property
#     def my_method(self):
#         return f"Передали " \
#                f"{self.p1}, {self.p2}"
#
#
# nc = MyClass("bla1", "text2")
# print(nc.my_method)


"""Свойства PROPERTY + SETTER"""

# class Auto:
#     def __init__(self, year):
#         self.year = year
#
#     @property
#     def year(self):
#         return self.__year
#
#     # сеттер для создания свойств
#     @year.setter
#     def year(self, year):
#         if year < 2000:
#             self.__year = 2000
#         elif year > 2019:
#             self.__year = 2019
#         else:
#             self.__year = year
#
#     def get_auto_year(self):
#         return f"Auto from {str(self.__year)}"
#
#
# a = Auto(2090)
# print(a.get_auto_year())

"""Композиция"""

# class WindowDoor:
#     def __init__(self, wd_len, wd_height):
#         self.square = wd_len * wd_height
#
#
# class Room:
#     def __init__(self, l1,l2, height):
#         self.square = 2 * height * (l1+l2)
#         self.wd = []
#
#     def add_win_door(self, wd_len, wd_height):
#         self.wd.append(WindowDoor(wd_len, wd_height))
#
#     def common_square(self):
#         main_sq = self.square
#         for el in self.wd:
#             main_sq -= el.square
#         return  main_sq
#
#
# room = Room(7, 4, 3.7)
# print(room.square)
# room.add_win_door(2,2)
# room.add_win_door(2,2)
# room.add_win_door(2,2)
# print(room.common_square())

"""Интерфейс итерации"""

#
# class Iterator:
#     """
#     Объект-итератор
#     """
#
#     def __init__(self, start=0):
#         self.i = start
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# class IterObj:
#     """"
#     Объект, поддерживающий интерфейс итерации
#     """
#
#     def __init__(self, start=0):
#         self.start = start - 1
#
#     def __iter__(self):
#         return Iterator(self.start)
#
#
# obj = IterObj(start=2)
# for el in obj:
#     print(el)

"""Оптимизируем"""

class Iter:
    def __init__(self, start = 0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


obj = Iter(start=2)
for el in obj:
    print(el)
print()

for el in obj:
    print(el)