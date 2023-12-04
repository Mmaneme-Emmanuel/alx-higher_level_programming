#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = 0
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero is undefined.")
            sys.exit(1)
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
