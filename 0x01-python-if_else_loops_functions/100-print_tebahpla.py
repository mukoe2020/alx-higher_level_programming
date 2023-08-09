#!/usr/bin/python3

h = 0
for j in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(j - h)), end="")
    h = 32 if h == 0 else 
