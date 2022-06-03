#!/usr/bin/python3
from sys import argv, exit

from calculator_1 import add, div, mul, sub

arg_len = len(argv)
if __name__ == "__main__":
    if arg_len < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    if operator == "+":
        a = int(argv[1])
        b = int(argv[3])
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == "-":
        a = int(argv[1])
        b = int(argv[3])
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == "*":
        a = int(argv[1])
        b = int(argv[3])
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == "/":
        a = int(argv[1])
        b = int(argv[3])
        print(f"{a} * {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
