#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('A') - ord('a')
            result += "{:c}".format(ord(char) + offset)
        else:
            result += char

    print(result)


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
