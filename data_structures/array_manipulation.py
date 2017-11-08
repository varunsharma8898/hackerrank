#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))

    n += 1
    arr = [0] * n
    for a0 in range(m):
        a, b, k = list(map(int, input().strip().split()))
        arr[a - 1] += k
        arr[b] -= k



    arr_sum = 0
    arr_max = 0
    for i in arr[:-1]:
        arr_sum += i
        arr_max = max(arr_sum, arr_max)

    print(arr_max)

'''
You are given a list(1-indexed) of size n, initialized with zeroes.
You have to perform m operations on the list and output the maximum of final values
of all the  elements in the list. For every operation, you are given three integers a, b and k
and you have to add value k to all the elements ranging from index a to b (both inclusive).

Output Format:
Print in a single line the maximum value in the updated list.

Sample Input:
5 3
1 2 100
2 5 100
3 4 100

Sample Output:
200
'''
