#!/usr/bin/python3
"""
This module defines a Square class.
The class handles size and position attributes with strict validation.
"""


class Square:
    """
    Defines a square by its size and position.

    Attributes:
        size (int): The width/height of the square.
        position (tuple): The (x, y) coordinates for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the square's sides.
            position (tuple): A tuple of 2 positive integers.
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
            value (int): The value to set as size.

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
        return self.__member_position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__member_position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character to stdout.
        Respects the position attribute for spacing.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y coordinate)
        # Note: We only print newlines if position[1] > 0
        for _ in range(self.__member_position[1]):
            print("")

        # Print each row of the square
        for _ in range(self.__size):
            # Print horizontal offset (x coordinate)
            print(" " * self.__member_position[0], end="")
            # Print the square row
            print("#" * self.__size)
