"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can not divide by 0.")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    try:
        math.log(a,b)# use math library/raise ValueError
    except ValueError as e:
        print(f"ValueError: {e}")
def exponent(a, b):
    a**b
