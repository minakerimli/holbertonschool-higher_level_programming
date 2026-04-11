#!/usr/bin/python3
"""
This module defines a Square class.
It includes size and position validation, area calculation,
and custom printing capabilities via my_print and __str__.
"""


class Square:
    """
    Defines a square by its size and position.

    Attributes:
        size (int): The side length of the square.
        position (tuple): The (x, y) coordinates for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character to stdout."""
        print(self.__str__())

    def __str__(self):
        """
        Defines the string representation of a Square instance.
        Matches the logic of my_print() for the print() function.

        Returns:
            The string representation of the square.
        """
        if self.__size == 0:
            return ""

        res = []
        # Handle the vertical offset (y-coordinate)
        for _ in range(self.__position[1]):
            res.append("")

        # Handle each row of the square
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
