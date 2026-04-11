#!/usr/bin/python3
"""
This module defines a Square class.
It supports area calculation and rich comparison operators
based on the area of the squares.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        size (number): The side length of the square (int or float).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (number): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (number): The new size.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if one square is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal to another in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if one square is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal to another in area."""
        return self.area() >= other.area()
