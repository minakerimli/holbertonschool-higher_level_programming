#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    """
    Import all functions from calculator_1 and perform basic operations.

    The program handles addition, subtraction, multiplication, and division
    based on command-line arguments. It validates the number of arguments
    and the operator type before execution.
    """
    # Number of arguments must be exactly 3 (excluding the script name)
    n_args = len(sys.argv) - 1
    if n_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assigning arguments to variables
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Mapping operators to the imported functions
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Validate if the operator is supported
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Calculate and print result
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
