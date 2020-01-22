#!/usr/bin/python3
"""
"""


class Student:

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            nlist = [k for k in attrs if hasattr(self, k)]
            return {k: getattr(self, k) for k in nlist}
        return self.__dict__
