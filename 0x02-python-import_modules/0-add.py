#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add

    # Assign values to variables a and b
    a = 1
    b = 2

    # Calculate the result
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
