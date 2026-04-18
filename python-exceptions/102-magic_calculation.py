#!/usr/bin/python3
"""Implements magic calculation based on given bytecode."""


def magic_calculation(a, b):
    """Replicate given bytecode logic."""
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = b + a
            break

    return result
