#!/usr/bin/env python3

# lib/functions.py


def greet_programmer():
    """Outputs a greeting to the programmer."""
    print("Hello, programmer!")


def greet(name):
    """Outputs a greeting to the specified name."""
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    """Outputs a greeting to the specified name, or defaults to 'programmer'."""
    print(f"Hello, {name}!")


def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def halve(number):
    """Returns the value of the number divided by two."""
    return number / 2
