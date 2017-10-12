#!/usr/bin/python3

mylist = []

N = int(input())

allowable_ops = [
    "insert",
    "print",
    "remove",
    "append",
    "sort",
    "pop",
    "reverse"
]

print(allowable_ops)

for x in range(N):
    line = input().split(" ")
    if line[0] in allowable_ops:
        if line[0] == 'insert':
            index = int(line[1])
            value = int(line[2])
            mylist[index:index] = [value]
        elif line[0] == 'print':
            print(mylist)
        elif line[0] == 'remove':
            mylist.remove(int(line[1]))
        elif line[0] == 'append':
            mylist.append(int(line[1]))
        elif line[0] == 'sort':
            mylist.sort()
        elif line[0] == 'pop':
            mylist.pop()
        elif line[0] == 'reverse':
            mylist.reverse()



'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''
