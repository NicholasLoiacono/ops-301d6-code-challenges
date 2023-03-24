#!/usr/bin/env python3

# Script: Ops 301d6 Class 09 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/23/2023
# Purpose: Python Conditional Statements
# Resources: Chat GPT


# Start

x = 5
y = 10

if x == y:
    print("x is equal to y")
elif x < y:
    print("x is less than y")
else:
    print("x is greater than y")

a = "hello"

if isinstance(a, int):
    print("a is an integer")
elif isinstance(a, str) and not a.isdigit():
    print("a is a string that is not a number")
else:
    print("a is not an integer or a non-numeric string")

h = 7

if h > 10:
    print("h is greater than 10")
elif h > 5:
    print("h is greater than 5 but not greater than 10")
else:
    print("h is not greater than 10 or 5")

# End