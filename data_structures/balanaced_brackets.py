#!/usr/bin/python3

import sys


def isValid(s):
    mystack = []
    bracket_map = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for x in (s):
        if mystack and bracket_map.get(x) == mystack[-1]:
            mystack.pop()
        else:
            mystack.append(x)

    # If stack is empty, it is balanced.
    return "YES" if not mystack else "NO"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isValid(s)
        print(result)

"""
Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output

YES
NO
YES


"""
