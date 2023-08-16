#!/usr/bin/python3
"""
the function returns a smiliar element in sets
the  loop iterates through the first set the for condition does the checkin
abd finally when a smilar element is found its added to the empty set
"""


def common_elements(set_1, set_2):
    common_set = set()

    for element in set_1:
        if element in set_2:
            common_set.add(element)

    return common_set
