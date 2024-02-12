class calculator:
    """This is a calculator class"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, object) -> None:
        return calculator(self.a + object.a, self.b + object.b)

    def __mul__(self, object) -> None:
        return calculator(self.a * object.a, self.b * object.b)

    def __sub__(self, object) -> None:
        return calculator(self.a - object.a, self.b - object.b)

    def __truediv__(self, object) -> None:
        return calculator(self.a / object.a, self.b / object.b)

    def __repr__(self):
        return "calculator(%s, %s)" % (self.a, self.b)
