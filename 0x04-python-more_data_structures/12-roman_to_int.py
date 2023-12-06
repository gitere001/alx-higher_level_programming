#!/usr/bin/python3
def calculate_subtraction_value(roman_values):
    to_subtract_value = 0
    max_roman_value = max(roman_values)

    for value in roman_values:
        if max_roman_value > value:
            to_subtract_value += value

    return (max_roman_value - to_subtract_value)


def roman_to_integer(roman_input):
    if not roman_input:
        return 0

    if not isinstance(roman_input, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_n.keys())

    result = 0
    last_roman_value = 0
    roman_values = [0]

    for char in roman_input:
        for numeral in numeral_keys:
            if numeral == char:
                if roman_n.get(char) <= last_roman_value:
                    result += calculate_subtraction_value(roman_values)
                    roman_values = [roman_n.get(char)]
                else:
                    roman_values.append(roman_n.get(char))

                last_roman_value = roman_n.get(char)

    result += calculate_subtraction_value(roman_values)

    return result
