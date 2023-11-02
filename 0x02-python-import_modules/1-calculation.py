#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Perform addition and print the result
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))

    # Perform subtraction and print the result
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    # Perform multiplication and print the result
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    # Perform division and print the result
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
