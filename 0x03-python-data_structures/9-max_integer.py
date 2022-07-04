#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_num = my_list[0]
        for i in my_list:
            max_num = i if i > max_num else max_num
        return max_num
