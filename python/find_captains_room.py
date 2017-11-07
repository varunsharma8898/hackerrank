#!/usr/bin/python3

k, arr = int(input()), list(map(int, input().split()))

rooms_set = set(arr)

room_num = ((sum(rooms_set) * k) - (sum(arr))) // (k - 1)

print(room_num)
