#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3 (total 4 with script name)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Casting arguments and identifying operator
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    # Comparison logic for operators
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        # Exact error message required by the task
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Formatted output
    print("{} {} {} = {}".format(a, op, b, result))
