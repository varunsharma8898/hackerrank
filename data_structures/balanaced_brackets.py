#!/usr/bin/python3

import sys

left_brackets = list("([{")
right_brackets = {
    '[': ']',
    '{': '}',
    '(': ')'
}

def isBalanced(s):
    mystack = []
    balanced = 1
    for char in list(s):
        if balanced == 0:
            continue

        if char in left_brackets:
            mystack.append(char)
        else:
            if right_brackets[mystack[-1]] == char:
                mystack.pop()
                continue
            else:
                balanced = 0

    return "YES" if balanced == 1 else "NO"

def isValid(s):
    mystack = []
    bracket_map = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    for x in (s):
        if not mystack:
            mystack.append(x)
        elif bracket_map[]:



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
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
