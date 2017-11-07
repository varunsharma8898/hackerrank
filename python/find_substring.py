#!/usr/bin/python3


# using list comprehension here to generate 1s for every match with substring in string
def count_substring(string, sub_string):
    return sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string])


if __name__ == '__main__':
    string = input()
    sub_string = input()

    count = count_substring(string, sub_string)
    print(count)
