#!/usr/bin/python3
'''
Reads n lines of a file
'''


def read_lines(filename="", nb_lines=0):
    '''
    Reads n lines of a file and print them
    '''
    txt = []
    with open(filename, mode='r', encoding='utf-8') as filet2:
        txt = filet2.readlines()
    numberLines = len(txt)
    if nb_lines <= 0 or nb_lines >= numberLines:
        for item in txt:
            print(item, end='')
    else:
        for i in range(nb_lines):
            print(txt[i], end='')
