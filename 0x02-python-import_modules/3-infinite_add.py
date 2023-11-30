#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    # Skip the first element (script name) and iterate over the rest
    for i in sys.argv[1:]:
        total_sum += int(i)
    print("{}".format(total_sum))
