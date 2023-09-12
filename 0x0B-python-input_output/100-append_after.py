#!/usr/bin/python3
"""
a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function for insertion of the line of text"""
    the_text = ""
    with open(filename) as h:
        for everyline in h:
            the_text += everyline
            if search_string in everyline:
                the_text += new_string
    with open(filename, "w") as m:
        m.write(the_text)
