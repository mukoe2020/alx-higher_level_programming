#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    initial_res = 0

    for argument in sys.argv:
        if argument != sys.argv[0]:
            initial_res += int(argument)
    print(initial_res)
