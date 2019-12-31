#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        nlist = my_list.copy()
        for i in range(len(nlist)):
            if i == idx:
                nlist[i] = element
                return nlist
