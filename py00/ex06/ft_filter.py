def ft_filter(func: bool, sequence: list):
    ret = []
    for i in sequence:
        if func(i) == True:
            ret.append(i)
    return ret


def main():
    list = ["A", "b", "C", "d", "E", "f", "G", "h", "I", "j"]
    fList = ft_filter(lambda x: x.isupper(), list)
    print("Original list: ", list)
    print("Filtered list: ", fList)
    return


if __name__ == "__main__":
    main()
