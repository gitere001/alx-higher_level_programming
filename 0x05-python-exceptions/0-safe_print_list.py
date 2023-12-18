#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_printed = 0
    
    try:
        for i in range(x):
            element = my_list[i]
            print(element, end=' ')
            element_printed += 1
    except IndexError:
        print("IndexError: Index is out of range")
    finally:
        print()
    return element_printed
