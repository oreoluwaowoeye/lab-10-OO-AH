#Link: https://github.com/oreoluwaowoeye/lab-10-OO-AH.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#Partner 1: Oreoluwa Owoeye
#Partner 2: Austin Henneberg


import math

# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    try:
        math.log(a,b)# use math library/raise ValueError
    except ValueError as e:
        print(f"ValueError: {e}")
def exponent(a, b):
    a**b

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
    if b < 0:
        raise ValueError("Base can not be negative.")
    return math.log(a, b)# use math library + raise ValueError

def exp(a, b):
    return a**b

def square_root(b):
    if a<0:
        raise ValueError("Must be positive.")
    return math.sqrt(b)

def hypotenuse(a, b):
    return math.sqrt(a**2+b**2)
