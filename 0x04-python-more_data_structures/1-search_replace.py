#!/usr/bin/python3
"""
this function will replace the occurences of the the selected item
the for loop will iterate through each element and the if statement will
find if the slected element is there and replace
"""


def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
