#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
if number < 0:
    i = -number
last = i % 10
if last < 0:
    last = -last
print("Last digit of {:d} is {:d} ".format(number, last), end='')
if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
