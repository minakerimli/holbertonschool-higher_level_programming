#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    """
    Handles basic arithmetic operations based on command-line arguments.
    Usage: ./100-my_calculator.py <a> <operator> <b>
    """
    # Check the number of arguments (including the script name, we expect 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Map operators to their respective functions
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Validate the operator and perform the calculation
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
