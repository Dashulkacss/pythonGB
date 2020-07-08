class ComplexNumber():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b),
                             self.a * other.b + self.b * other.a)

    def __str__(self):
        if self.b < 0:
            return f"z = {self.a}{self.b}i"
        else:
            return f"z = {self.a} + {self.b}i"


cn1 = ComplexNumber(3, 4)
cn2 = ComplexNumber(5, -6)
print(cn1)
print(cn2)
print(f"Сумма комплексных чисел: {cn1 + cn2}")
print(f"Произведение комплексных чисел: {cn1 * cn2}")
