#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check the number of arguments (Script + 3 args = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assign and cast variables
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    # Handle operations based on the operator string
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        # Error message if the operator is not recognized
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result in the format: <a> <operator> <b> = <result>
    print("{} {} {} = {}".format(a, op, b, result))
