#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list.copy()
    for i, j in enumerate(my_list):
        if j == search:
            nlist[i] = replace
    return nlist
