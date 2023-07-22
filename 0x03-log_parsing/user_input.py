#!/usr/bin/python3

import os
import sys

'''Initialize an empty list to store the lines of input'''
user_input = []

'''Read the input line by line until an empty line is entered'''
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    user_input.append(line)

'''Display the lines of input back to the user'''
print("You entered the following lines:")
for line in user_input:
    print(line)

'''Calculate the average length of the lines'''
total_length = sum(len(line) for line in user_input) 
average_length = total_length / len(user_input)

'''Print the computed Metrics'''
print("Average line length:", average_length)
