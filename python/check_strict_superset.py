#!/usr/bin/python3

arr = set(map(int, input().split()))

fail_count = 0

for i in range(int(input())):
    test_arr = set(map(int, input().split()))
    test_status = 0
    if len(test_arr) < len(arr):
        test_status = sum([1 if i not in arr else 0 for i in test_arr])
        fail_count += 1 if test_status > 0 else 0
    else:
        fail_count += 1

    # if test_status > 0:
    #     print('fail')
    # else:
    #     print('pass')

print(False if fail_count > 0 else True)
