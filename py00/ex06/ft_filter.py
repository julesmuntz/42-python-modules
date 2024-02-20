def ft_filter(func, it):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for \
which function(item) is true. If function is None, return the \
items that are true.
    """
    if func is None:
        return [x for x in it if x]
    return [x for x in it if func(x)]


def main():
    list = ["A", "b", "C", "d", "E", "f", "G", "h", "I", "j"]
    fList = ft_filter(lambda x: x.isupper(), list)
    print("Original list: ", list)
    print("Filtered list: ", fList)
    return


if __name__ == "__main__":
    main()
