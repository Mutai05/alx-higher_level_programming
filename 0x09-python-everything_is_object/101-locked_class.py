#!/usr/bin/python3

class LockedClass:
    """LockedClass that restricts the creation of new instance attributes except 'first_name'."""
    
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
