#!/bin/bash

# Script: Ops 301d6 Class 02 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/14/2023
# Purpose: Time Stamping
# Resources: Chat GPT


# Main

# Define the filename
filename="syslog_$(date +%Y-%m-%d_%H-%M-%S)"

# Provide feedback to the user
echo "Copying /var/log/syslog to ${filename}..."

# Copy the file and append the timestamped filename
cp /var/log/syslog ./${filename}

# Provide feedback to the user
echo "File copied to ${filename}"

# End