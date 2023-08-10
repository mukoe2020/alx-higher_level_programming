#!/usr/bin/env python3

import sys


def main():
    argv = sys.argv[1:]
    total_sum = sum(int(arg) for arg in argv)

    print("Sum of arguments: {}".format(total_sum))


if __name__ == "__main__":
    main()
