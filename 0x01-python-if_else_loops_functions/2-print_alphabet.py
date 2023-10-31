#!/usr/bin/python3

# ASCII value of 'a' and 'z'
ascii_a = ord('a')
ascii_z = ord('z')

# Loop to print the lowercase alphabet
for char_ascii in range(ascii_a, ascii_z + 1):
    print("{:c}".format(char_ascii), end="")

# Print a newline character at the end
print()
