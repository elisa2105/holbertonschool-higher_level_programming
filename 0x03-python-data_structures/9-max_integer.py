#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        i = my_list[0]
        for number in my_list:
            if number > i:
                i = number
    return i
