from abc import ABC, abstractclassmethod


class Clothes(ABC):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    @abstractclassmethod
    def count_consumption(cls):
        pass

    def get_params(self):
        return self.params

    def __add__(self, other):
        return self.count_consumption() + other.count_consumption()


class Coat(Clothes):

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, params):
        if params > 100:
            self.__params = 100
        elif params < 13:
            self.__params = 13
        else:
            self.__params = params

    def count_consumption(self):
        return (self.get_params() / 6.5) + 0.5


class Suit(Clothes):

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, params):
        if params > 2:
            self.__params = 2
        elif params < 1.4:
            self.__params = 1.4
        else:
            self.__params = params

    def count_consumption(self):
        return 2 * self.get_params() + 0.3


coat1 = Coat("Пальтишко", 20)
suit1 = Suit("Костюмишко", 1.8)
print(f"Длина {coat1.name} : {coat1.get_params()}")
print(f"Расход ткани: {coat1.count_consumption()}")
print(f"Длина {suit1.name} : {suit1.get_params()}")
print(f"Расход ткани: {suit1.count_consumption()}")
print(f"Расход ткани общий: {coat1 + suit1}")
coat1.count_consumption()
