#!/usr/bin/python3
# 103-magic_class.py by Kelvin KIpkemboi
"""class MagicClass """

class MagicClass:
    """set up magic class"""
    
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
