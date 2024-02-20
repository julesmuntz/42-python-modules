class calculator:
    """This is a calculator class"""

    def __init__(self, values):
        """Constructor for the calculator class."""
        self.values = values

    def __add__(self, object) -> None:
        """Addition method"""
        self.values = [value + object for value in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiplication method"""
        self.values = [value * object for value in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """Substraction method"""
        self.values = [value - object for value in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """Division method"""
        try:
            self.values = [value / object for value in self.values]
            print(self.values)
        except ZeroDivisionError:
            print("Error: division by zero")

    def __repr__(self):
        """Representation of the calculator class."""
        return f"{self.values}"
