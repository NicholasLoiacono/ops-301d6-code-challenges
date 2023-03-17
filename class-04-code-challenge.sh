#!/bin/bash

# Script: Ops 301d6 Class 04 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/16/2023
# Purpose: Menu Options with Loop
# Resources: Chat GPT


# Main

while true
do
    echo "Please select an option:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read choice

    case $choice in
        1) echo "Hello world!";;
        2) ping 127.0.0.1;;
        3) ifconfig;;
        4) exit;;
        *) echo "Invalid choice. Please enter a valid option.";;
    esac
done

# End