#!/bin/env python3

d = {}

with open('file.txt') as inf:
    for line in inf:
        my_list = line.lower().split()
        for word in my_list:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

v = 0
for key, value in d.items():
    if value > v:
        k = key
        v = value
    elif value == v and key < k:
        k = key
        v = value
print(k, v)
