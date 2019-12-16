#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(len(argv)):
        if i != 0:
            sum += int(argv[i])
    print("{}".format(sum))
