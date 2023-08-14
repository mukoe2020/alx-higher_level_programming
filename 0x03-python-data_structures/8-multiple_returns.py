#!/usr/bin/python3
"""
The multiple_returns function takes a sentence string as input.
- It calculates the length of the string using the len() function and assigns
it to the length variable.
- If the length of the sentence is 0 (empty string), the first character
is set to None.
- Otherwise, the first character is assigned as the first character of the
sentence, sentence[0].
- Finally, it returns a tuple with the length and first character.
"""


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return length, first
