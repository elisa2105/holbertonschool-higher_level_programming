#!/usr/bin/python3
'''
Returns the number of lines in a txt
'''


def number_of_lines(filename=""):
    '''
    Returns the number of lines in a txt
    '''
    numberLines = 0
    with open(filename, mode='r', encoding='utf-8') as filet1:
        for line in filet1:
            numberLines += 1
    return numberLines
