class calculator:
    """This is a calculator class"""

    def __init__(self, values):
        self.values = values

    def __add__(self, object) -> None:
        self.values = [value + object for value in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        self.values = [value * object for value in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        self.values = [value - object for value in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        try:
            self.values = [value / object for value in self.values]
            print(self.values)
        except ZeroDivisionError:
            print("Error: division by zero")

    def __repr__(self):
        return f"{self.values}"
