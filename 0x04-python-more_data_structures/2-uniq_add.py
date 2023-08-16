#!/user/bin/python3
"""
this is a function to add uniq intergers
i start by creating an empty set and checki f the integer is not alredy added
and add interger to the list and finally test the funnction
"""


def uniq_add(my_list=[]):
    unique_integers = set()
    total_sum = 0

    for num in my_list:
        if num not in unique_integers:
            total_sum += num
            unique_integers.add(num)

    return total_sum


