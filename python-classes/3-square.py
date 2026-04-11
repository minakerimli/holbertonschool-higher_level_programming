#!/usr/bin/python3
"""Defines a Square class with size validation and area computation."""


class Square:
    """Represents a square with a validated size and area method."""

    def __init__(self, size=0):
        """Initialize square with optional validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
