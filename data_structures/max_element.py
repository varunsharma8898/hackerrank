#!/usr/bin/python3

# Brute force way, fails for time constrained tests
# should use a max_array for this.

mystack = []
max_num = 0
for i in range(int(input())):
    op, *num = input().split()
    op = int(op)

    if op == 1:
        num = int(num[0])
        mystack.append(num)
        if max_num < num:
            max_num = num
    elif op == 2:
        mystack.pop()
    else:
        print(max(mystack))



"""
You have an empty sequence, and you will be given queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

Input Format:
The first line of input contains an integer, . The next lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Output Format:
For each type query, print the maximum element in the stack on a new line.

Sample Input:

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3

Sample Output:

26
91
"""