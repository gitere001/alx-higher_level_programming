#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_elment = my_list[0]
    for i in my_list[1:]:
        if i > max_elment:
            max_elment = i
    return max_elment
