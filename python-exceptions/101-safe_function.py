#!/usr/bin/python3
"""Safely execute a function and handle exceptions."""

import sys


def safe_function(fct, *args):
    """Execute function safely and return result or None."""
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
