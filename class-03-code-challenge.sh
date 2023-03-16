#!/bin/bash

# Script: Ops 301d6 Class 03 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/15/2023
# Purpose: Alter input inside files
# Resources: Chat GPT


# Main

# Prompt user for input directory path
echo "Please enter the directory path:"
read directory

# Prompt user for input permissions number
echo "Please enter the new permissions number (e.g. 777):"
read permissions

# Navigate to the directory input by the user and change all files inside it to the input setting
cd $directory
chmod -R $permissions *

# Print to the screen the directory contents and the new permissions settings of everything in the directory
echo "Directory contents:"
ls -l $directory

# End