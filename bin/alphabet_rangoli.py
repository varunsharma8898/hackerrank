#!/usr/bin/python3

alphabets = tuple('abcdefghijklmnopqrstuvwxyz')


def print_rangoli(size):
    max_width = size * 2 - 1
    print_width = max_width * 2 - 1

    # Initialize the array that will hold all the rows to print
    arr = [None] * max_width

    # the list of characters that will be used to generate rows
    # ex. a, b, c, d
    mid_arr = list(alphabets[:size])

    for i in range(size):
        ref_arr = mid_arr[i:]
        arr1 = list(ref_arr[::-1])     # reverse the ref_arr
        arr1.extend(ref_arr[1:])       # copy ref_arr contents except the 0th element

        if (size + i - 1) < max_width: arr[size + i - 1] = arr1
        if (size - i - 1) > -1: arr[size - i - 1] = arr1

    for row in arr:
        str = '-'.join(row)
        str = str.center(print_width, '-')
        print(str)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''
https://www.hackerrank.com/challenges/alphabet-rangoli

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''