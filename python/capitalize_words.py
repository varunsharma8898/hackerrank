#!/usr/bin/python3
import re


# Brute-force way to capitalize string
# Cannot use string.capitalize on string.split here
# coz there can be multiple spaces between each word
def capitalize(string):
    char_arr = []
    prev_char = 1
    for char in list(string):
        char_arr.append(char)

        if re.match(r'\s', char) or (prev_char == 1 and re.match(r'\s', char)):
            prev_char = 1
            continue

        if prev_char == 1 and re.match(r'\w', char):
            char_arr.append(str(char_arr.pop()).capitalize())
            prev_char = 0

    return "".join(char_arr)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
