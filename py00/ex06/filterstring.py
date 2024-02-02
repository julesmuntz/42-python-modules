import sys


def main():
	if len(sys.argv) != 3 or (not sys.argv[1].isalnum() and not sys.argv[2].isdigit()):
		return print("AssertionError: the arguments are bad")
	list = []
	list.append(str(sys.argv[1]))
	list.append(int(sys.argv[2]))
	print(list)
	return


if __name__ == "__main__":
	main()
