class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": income[0], "bonus": income[1]}


class Position(Worker):

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(self._Worker__income.get("wage") + self._Worker__income.get("bonus"))


worker1 = Position("Ivan", "Ivanov", "Master Data Analyst", [20000, 5000])

print(f"Name: {worker1.name}")
print(f"Surname: {worker1.surname}")
print(f"Position: {worker1.position}")
print(f"Income: {worker1._Worker__income}")

print()
worker1.get_full_name()
worker1.get_total_income()
