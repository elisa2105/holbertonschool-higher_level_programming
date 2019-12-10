#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        s = str[:n] + str[n + 1:]
        return s
    else:
        return str
