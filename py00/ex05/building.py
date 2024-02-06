import sys


def main():
    prompt = False
    if len(sys.argv) < 2:
        for line in sys.stdin:
            string = line
        prompt = True
    if len(sys.argv) == 2 or prompt is True:
        upper = 0
        lower = 0
        punct = 0
        space = 0
        digit = 0
        for i in string:
            if i.isupper():
                upper = upper + 1
            elif i.islower():
                lower = lower + 1
            elif i.isspace():
                space = space + 1
            elif i.isdigit():
                digit = digit + 1
            else:
                punct = punct + 1
        print("The text contains", len(string), "characters:")
        print(upper, "upper letters")
        print(lower, "lower letters")
        print(punct, "punctuation marks")
        print(space, "spaces")
        print(digit, "digits")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")


if __name__ == "__main__":
    main()
