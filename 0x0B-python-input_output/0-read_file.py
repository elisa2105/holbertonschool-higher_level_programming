#!/usr/bin/python3
'''
Reads a txt file and prints it
'''


def read_file(filename=""):
    '''
    Read an UTF-8 encode file and print it
    '''
    with open(filename, mode='r', encoding='utf-8') as filet0:
        contents = filet0.read()
    print(contents, end='')
