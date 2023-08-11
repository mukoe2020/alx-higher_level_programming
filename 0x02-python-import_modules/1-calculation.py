#!/usr/bin/python3
if __name__ == "__main__":
    # Your program should call each of the imported functions.
    from calculator_1 import add, sub, mul, div

    # a and b must be defined in 2 different lines: a = 10 and another b = 5
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
