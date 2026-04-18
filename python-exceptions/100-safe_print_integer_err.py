#!/usr/bin/python3
"""Safely print an integer and handle errors."""

import sys


def safe_print_integer_err(value):
    """Print an integer safely using format, handle exceptions."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
