import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        return print("AssertionError: the arguments are bad")
    try:
        if ft_filter(lambda x: not x.isalnum(), sys.argv[1].split()):
            return print(
                "AssertionError: 1st arg must not contain any special \
                    characters (Punctuation or invisible)"
            )
        string = ft_filter(
            lambda x: len(x) >= int(sys.argv[2]), sys.argv[1].split())
        print(list(string))
        return
    except ValueError:
        return print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
