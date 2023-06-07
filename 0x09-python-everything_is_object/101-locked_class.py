#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        self.__dict__[key] = value
