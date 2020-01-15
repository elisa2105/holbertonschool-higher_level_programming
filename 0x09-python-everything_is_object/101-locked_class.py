#!/usr/bin/python3
""" LockedClass """


class LockedClass:
    """ Class with no attributes """
    def __setattr__(self, attribName, value):
        """ Called when an attribute assignment is attempted."""
        if attribName == "first_name":
            self.__dict__[attribName] = value
        else:
            msg = "'LockedClass' object has no attribute '" + attribName + "'"
            raise AttributeError(msg)
