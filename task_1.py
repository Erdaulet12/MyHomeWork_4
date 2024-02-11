"""task_1.py"""


class Circle:
    """Overloaded circle methods"""

    def __init__(self, radius):
        """initial method"""
        self.radius = radius

    def __eq__(self, other):
        """equal method"""
        return self.radius == other.radius

    def __lt__(self, other):
        """"less" method"""
        return self.radius < other.radius

    def __le__(self, other):
        """"less or equal" method"""
        return self.radius <= other.radius

    def __gt__(self, other):
        """"more" method"""
        return self.radius > other.radius

    def __ge__(self, other):
        """"more or equal" method"""
        return self.radius >= other.radius

    def __add__(self, other):
        """sum method"""
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        """substract method"""
        return Circle(self.radius - other.radius)

    def __iadd__(self, other):
        """iadd method"""
        self.radius += other.radius
        return self

    def __isub__(self, other):
        """isub method"""
        self.radius -= other.radius
        return self


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = c1 + c2
    c1 -= c2
    print(c1 == c2)
    print(c1 < c2)
    print(c1 <= c2)
    print(c1 > c2)
    print(c1 >= c2)

    print(c3.radius)
    print(c1.radius)
