#!/usr/bin/python3


def print_formatted(n):
    # find out binary value of n and use it's length as max_width
    max_width = len(bin(n)[2:])
    max_width += 1

    for i in range(n):
        str = ""

        # format number to decimal
        str1 = "{num:d}".format(num=i + 1)
        str1 = str1.rjust(max_width-1)
        str += str1

        # format number to octal
        str2 = "{num:o}".format(num=i + 1)
        str2 = str2.rjust(max_width)
        str += str2

        # format number to hexadecimal
        str3 = "{num}".format(num=hex(i+1)[2:])
        str3 = str3.rjust(max_width)
        str += str3.upper()

        str4 = "{num:b}".format(num=i + 1)
        str4 = str4.rjust(max_width)
        str += str4

        print(str)

'''
Given an integer, N, print the following values for each integer  from 1 to N:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to N.
Each value should be space-padded to match the width of the binary value of N.

'''

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)