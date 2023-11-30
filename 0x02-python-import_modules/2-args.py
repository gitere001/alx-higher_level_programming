#!/usr/bin/python3

if __name__ == "__main__":
    """print the number plus list of arguments."""
    import sys
    number_of_arguments = len(sys.argv) - 1
    if number_of_arguments == 0:
        print("0 arguments.")
    elif number_of_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments".format(number_of_arguments))
    for i in range(number_of_arguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
