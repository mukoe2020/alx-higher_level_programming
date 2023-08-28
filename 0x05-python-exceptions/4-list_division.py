#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 1

            if type(elem_1) not in (int, float) or type(elem_2) not in (int, float):
                print("wrong type")
                result.append(0)
            elif elem_2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(elem_1 / elem_2)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

    return result
