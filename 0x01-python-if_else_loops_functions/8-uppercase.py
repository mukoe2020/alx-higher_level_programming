#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('A') - ord('a')
            print("{:c}".format(ord(char) + offset), end='')
        else:
            print(char, end='')

    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
