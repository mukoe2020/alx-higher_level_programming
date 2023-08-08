#!/usr/bin/python3
output = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in ['q', 'e']:
        output += chr(i)

print("{}".format(output), end='')
