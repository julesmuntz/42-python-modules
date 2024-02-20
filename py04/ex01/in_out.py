def square(x: int | float) -> int | float:
    """Returns the square of the number passed as argument"""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the power of the number passed as argument"""
    return x**x


def outer(x: int | float, function) -> object:
    """Function that takes as argument a number and a function, \
it returns an object that when called returns the result of the \
arguments calculation."""
    count = 0

    def inner() -> float:
        """Function that takes no arguments and returns the result of \
the arguments calculation."""
        nonlocal count
        res = function(x)
        for _ in range(count):
            res = function(res)
        count += 1
        return res

    return inner
