class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
        return f"{self._numerator} / {self._denominator}"

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def invert(self):
        return Fraction(self.denominator, self.numerator)


if __name__ == '__main__':
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)
    print(fraction1)
    print(fraction2)
    print(fraction1 + fraction2)
    print(fraction2 - fraction1)
    print(fraction1.invert())
