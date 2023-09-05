#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]

            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                raise TypeError("wrong type")

            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = elem_1 / elem_2
            result.append(division_result)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
