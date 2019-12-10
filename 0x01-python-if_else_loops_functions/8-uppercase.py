#!/usr/bin/python3
def uppercase(str):
    for character in range(len(str)):
        letter = ord(str[character])
        if str[character].islower():
            letter = letter - 32
        letter = chr(letter)
        print("{}".format(letter), end="")
    print()
