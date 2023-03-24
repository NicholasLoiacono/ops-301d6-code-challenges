#!/usr/bin/env python3

# Script: Ops 301d6 Class 10 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/24/2023
# Purpose: Python File Handling
# Resources: Chat GPT


# Start

# Open file for appending
file = open("demo.txt", "a")

# Append three lines to the file
file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.write("This is line 3.\n")

# Close the file
file.close()

# Open file for reading
file = open("demo.txt", "r")

# Read the first line and print to the screen
print(file.readline())

# Close the file
file.close()

# Delete the file
import os
os.remove("demo.txt")

# End