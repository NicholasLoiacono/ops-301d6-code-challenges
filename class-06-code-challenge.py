#!/usr/bin/env python3
#!/bin/bash

# Script: Ops 301d6 Class 06 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/20/2023
# Purpose: Original Python Demo Code Challenge
# Resources: Chat GPT

# Main

import os

# execute the "whoami" bash command and store the output in a variable
whoami_output = os.popen('whoami').read().strip()

# execute the "ip a" bash command and store the output in a variable
ip_output = os.popen('ip a').read().strip()

# execute the "lshw -short" bash command and store the output in a variable
lshw_output = os.popen('lshw -short').read().strip()

# print the output of the "whoami" command
print("Output of 'whoami' command:")
print(whoami_output)

# print the output of the "ip a" command
print("\nOutput of 'ip a' command:")
print(ip_output)

# print the output of the "lshw -short" command
print("\nOutput of 'lshw -short' command:")
print(lshw_output)

# End