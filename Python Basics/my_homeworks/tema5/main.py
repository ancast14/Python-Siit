class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError
        self.__simplify()

    def __simplify(self):
        gcd = self.__gcd(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    def __gcd(self, a, b):
        if b == 0:
            return a
        return self.__gcd(b, a % b)

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

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
    fraction1 = Fraction(2, 0)
    fraction2 = Fraction(3, 4)
    print(fraction1)
    print(fraction2)
    print(fraction1 + fraction2)
    print(fraction2 - fraction1)
    print(fraction1.invert())

    fraction3 = Fraction(0, 2)
    fraction4 = Fraction(3, 4)
    print(fraction3)
    print(fraction4)
    print(fraction3 + fraction4)
    print(fraction4 - fraction3)
    print(fraction3.invert())

    fraction5 = Fraction(2, 4)
    fraction6 = Fraction(3, 4)
    print(fraction5)
    print(fraction6)
    print(fraction5 + fraction6)
    print(fraction6 - fraction5)
    print(fraction5.invert())

    x = Fraction(2, 4)
    assert x.numerator == 1
    assert x.denominator == 2

    assert x._Fraction__numerator == 1
    assert x._Fraction__denominator == 2