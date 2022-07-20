#!/usr/bin/python3
"""2-square.py"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
