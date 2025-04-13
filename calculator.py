"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can not divide by zero.")
    return b / a

def log(a, b):
    try:
        return log(a, b)# use math library + raise ValueError
    except ValueError as e:
        print(f"ValueError as {e}")

def exp(a, b):
    return a**b