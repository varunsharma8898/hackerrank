#!/usr/bin/python3

string = input()
[index_to_update, replacement] = input().split(" ")

str_list = list(string)
str_list[int(index_to_update)] = replacement[0]
print(''.join(str_list))

'''
Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, . 
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format 
Using any of the methods explained above, replace the character at index  with character .

'''