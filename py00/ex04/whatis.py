import sys

def main():
    if len(sys.argv) < 2:
        return
    if len(sys.argv) > 2:
        return print("AssertionError: more than one argument is provided")
    try:
        int(sys.argv[1])
    except:
        return print("AssertionError: argument is not an integer")
    if (int(sys.argv[1]) % 2) == 0:
        return print("I'm Even.")
    if (int(sys.argv[1]) % 2):
        return print("I'm Odd.")

if __name__ == "__main__":
    main()