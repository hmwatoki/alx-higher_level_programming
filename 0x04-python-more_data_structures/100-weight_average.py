#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        num, denom = 0, 0
        for t in my_list:
            num += t[0] * t[1]
            denom += t[1]
        return num/denom
