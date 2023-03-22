#!/usr/bin/env python3

# Script: Ops 301d6 Class 07 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/21/2023
# Purpose: Generate all directories and files
# Resources: Chat GPT


# Start

# Import libraries

import os

# Declaration of variables


### Read user input here into a variable
path =  input("Enter a file path: ")

# Declaration of functions

### Declare a function here
def generate_directory_tree(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
    ### Add a print command here to print ==root==
        print(root)
        for dir in dirs:
        ### Add a print command here to print ==dirs==
            print(dirs)
        for file in files:
        ### Add a print command here to print ==files==
            print(files)
        ### Newline character
            print("\n")

# Main

### Pass the variable into the function here

generate_directory_tree(directory_path)

# End