#!/usr/bin/python3
'''
Triangle
'''


def pascal_triangle(n):
    '''
    Creates the triangle and returns the matrix
    '''
    pas = []
    for i in range(n):
        row = [0] * (i + 1)
        row[0] = 1
        row[i] = 1
        if i > 1:
            row[1] = i
            row[i - 1] = i
        while 0 in row:
            index = row.index(0)
            number = pas[i - 1][index] + pas[i - 1][index - 1]
            row[index] = number
        pas.append(row)
    return pas
