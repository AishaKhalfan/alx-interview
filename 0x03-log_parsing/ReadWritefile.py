#!/usr/bin/python3
import sys
import os

# Reading the contents from "0-generator.py"
with open("0-generator.py", "r") as file:
    contents = file.read()
#    print(contents)

# Writing the contents to another text file
with open("output.txt", "w") as output_file:
    output_file.write(contents)

print("Contents have been written to 'output.txt' successfully.")

