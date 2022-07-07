#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mul_num = 1
        sum_num = 0
        sum_num2 = 0
        for row in my_list:
            for col in row:
                mul_num *= col
            sum_num += mul_num
            mul_num = 1
            sum_num2 += row[-1]
        return float(sum_num / sum_num2)
    else:
        return 0
