"""task_4.py"""

class Flat:
    """flat class"""
    def __init__(self, area, price):
        """initial method"""
        self.area = area
        self.price = price

    def __eq__(self, other):
        """equal method"""
        return self.area == other.area

    def __ne__(self, other):
        """not equal method"""
        return self.area != other.area

    def __gt__(self, other):
        """more method"""
        return self.price > other.price

    def __lt__(self, other):
        """less method"""
        return self.price < other.price

    def __le__(self, other):
        """less or equal method"""
        return self.price <= other.price

    def __ge__(self, other):
        """more or equal method"""
        return self.price >= other.price

    def __str__(self):
        """check method"""
        return f"Квартира ({self.area} м², {self.price} руб.)"


if __name__ == "__main__":
    flat1 = Flat(50, 1000000)
    flat2 = Flat(60, 1200000)

    print(flat1 == flat2)
    print(flat1 != flat2)
    print(flat1 > flat2)
    print(flat1 < flat2)
    print(flat1 <= flat2)
    print(flat1 >= flat2)
    print(flat1)
    print(flat2)
