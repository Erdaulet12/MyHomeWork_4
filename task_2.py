"""task_1.py"""


class Complex:
    """Complex numbers"""

    def __init__(self, real, imag):
        """inital method"""
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """add method"""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """substract method"""
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """multi method"""
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        """truediv method"""
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __str__(self):
        """string method"""
        return f"{self.real} + {self.imag}j"


if __name__ == "__main__":

    c1 = Complex(2, 3)
    c2 = Complex(4, 5)

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
