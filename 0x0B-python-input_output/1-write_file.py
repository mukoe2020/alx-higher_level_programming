#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as i:
        return i.write(text)
