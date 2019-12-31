#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for i in my_string:
        if i == 'c':
            my_string.remove('c')
        elif i == 'C':
            my_string.remove('C')
        else:
            continue
    return ''.join(my_string)
