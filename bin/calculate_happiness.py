#!/usr/bin/python3

arr_len, set_len = map(int, input().split())

arr = list(map(int, input().split()))
set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))

happiness = sum([ 1 if i in set_1
                  else
                    -1 if i in set_2
                    else 0
                  for i in arr ])

print(happiness)