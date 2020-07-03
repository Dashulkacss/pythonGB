class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculated(self):
        return self._length * self._width * 25 * 5 / 1000


road1 = Road(20, 5000)
print(f"Масса асфальта {road1.calculated()} т")
