#!/usr/bin/python3
"""
Find the peak in a unsorted integers list
"""


def find_peak(list_of_integers):
    """
    Finds the pick in a list
    :list_of_integers: list
    :return: peak
    """
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    return list_of_integers[peak(list_of_integers, 0,
                                 len(list_of_integers) - 1)]


def peak(ints, left, right):
    """
    search the peak
    :ints: list
    :left: left
    :right: right
    :return: position of the peak
    """
    if left == right:
        return left
    mid = int((left + right) / 2)
    if ints[mid] > ints[mid + 1]:
        return peak(ints, left, mid)
    return peak(ints, mid + 1, right)
