#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a square."""
    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method for area of square."""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of this square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
