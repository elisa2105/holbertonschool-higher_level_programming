#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        i = roman_string
        j = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for k in range(len(i)):
            for l, m in j.items():
                if k == i[k]:
                    if k + 1 < len(i) and j[i[k + 1]] > j[i[k]]:
                        res -= m
                    else:
                        res += m
        return res
    return 0
