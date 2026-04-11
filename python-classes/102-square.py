#!/usr/bin/python3
"""
This module defines a Square class.
It includes size validation and provides functionality to compare
different Square instances based on their calculated area.
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
            size (number): The size of the square's sides.
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
        Calculates the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square's area is less than another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square's area is less than or equal to another's."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square's area is greater than another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to another's."""
        return self.area() >= other.area()
