#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    """
    Handles basic arithmetic operations based on command-line arguments.

    The function checks for the correct number of arguments, validates
    the operator, performs the calculation using imported functions,
    and prints the result in the format: <a> <operator> <b> = <result>.
    """
    # Check the number of arguments (script name + 3 arguments = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Cast arguments to integers
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Map operators to their respective functions from calculator_1
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Validate if the operator exists in our dictionary
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the operation and print the result
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
