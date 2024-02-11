"""task_3.py"""


class Airplane:
    """Airplane class"""

    def __init__(self, model, max_passengers):
        """initial method"""
        self.model = model
        self.max_passengers = max_passengers
        self.passengers = 0

    def __eq__(self, other):
        """equal method"""
        return self.model == other.model

    def __add__(self, other):
        """add method"""
        return self.passengers + other.passengers

    def __sub__(self, other):
        """substract method"""
        return self.passengers - other.passengers

    def __iadd__(self, other):
        """iadd method"""
        self.passengers += other
        return self

    def __isub__(self, other):
        """isub method"""
        self.passengers -= other
        return self

    def __gt__(self, other):
        """more method"""
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        """less method"""
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        """less or equal method"""
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        """more or equal method"""
        return self.max_passengers >= other.max_passengers

    def __str__(self):
        """check method"""
        return f"{self.model} ({self.passengers}/{self.max_passengers})"


if __name__ == "__main__":
    first_plane = Airplane("Boeing 747", 467)
    second_plane = Airplane("Airbus A380", 853)

    print(first_plane == second_plane)
    print(first_plane + second_plane)
    print(first_plane - second_plane)
    first_plane += 100
    print(first_plane)
    first_plane -= 50
    print(first_plane)
    print(first_plane > second_plane)
    print(first_plane < second_plane)
    print(first_plane <= second_plane)
    print(first_plane >= second_plane)
