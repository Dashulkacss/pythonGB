class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"\nВжух вжух!, я {self.color} {self.name}!")
        print(f"{self.name} полицйская") if self.is_police else print(
            f"{self.name} не полицейская")
        self.show_speed()

    def go(self):
        return print(f"{self.name} поехала")

    def stop(self):
        return print(f"{self.name} остановилась")

    def turn(self, direction):
        return print(f"{self.name} повернула {direction}")

    def show_speed(self):
        return print(f"Скорость равна {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость равна {self.speed}")
        if self.speed > 60:
            return print("Вы превысили скорость!")


class SportCar(Car):
    description = "Very fast one"


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость равна {self.speed}")
        if self.speed > 40:
            return print("Вы превысили скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"\nВжух вжух!, я {self.color} {self.name}!")
        print(f"{self.name} полицйская") if self.is_police else print(
            f"{self.name} не полицейская")
        self.show_speed()


car_speed = SportCar(100, "желтая","Вжух")
car_for_work = WorkCar(61, "красная", "Ford")
car_for_police = PoliceCar(100, "синяя", "Виу Виу")
car_for_town = TownCar(61, "белая", "TownCar")
print()
car_for_town.go()
car_for_town.turn("налево")
car_for_town.stop()
