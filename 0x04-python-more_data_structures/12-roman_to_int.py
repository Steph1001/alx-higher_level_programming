#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = 0
    bol = True
    sub_num = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for n in range(len(roman_string)):
        if bol:
            for j in range(n, len(roman_string)):
                if roman[roman_string[n]] < roman[roman_string[j]]:
                    bol = False
                    break
        if not bol and n != j:
            sub_num += roman[roman_string[n]]
            continue
        bol = True
        num = num + (roman[roman_string[n]] - sub_num)
        sub_num = 0
    return num
