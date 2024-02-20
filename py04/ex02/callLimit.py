def callLimit(limit: int):
    """Decorator that takes an integer as argument and returns a decorator \
that takes a function as argument and returns a function that can only be \
called a certain number of times. If the function is called more than the \
limit, it prints an error message."""
    count = 0

    def callLimiter(function):
        """Decorator that takes a function as argument and returns a function \
that can only be called a certain number of times. If the function is called \
more than the limit, it prints an error message."""

        def limit_function(*args: any, **kwds: any):
            """Function that takes any number of arguments and returns the \
result of the function passed as argument if the number of calls is less \
than the limit, otherwise it prints an error message."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
