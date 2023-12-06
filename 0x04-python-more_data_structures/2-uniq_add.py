#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_numbers = set()
    for num in my_list:
        uniq_numbers.add(num)
    sum_uniq = sum(uniq_numbers)

    return sum_uniq
