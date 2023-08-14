#!/usr/bin/python3
"""
Initialize an empty string to store the modified string
Iterate over each character in the input string
Check if the lowercase version of the character is not equal to 'c'
If it's not 'c', concatenate the character to the new_string
Return the modified string without 'c' and 'C'
"""


def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
