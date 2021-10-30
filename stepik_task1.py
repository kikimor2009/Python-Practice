#!/bin/env python3

inf = open("/Users/macserebro/Downloads/file.txt")
s = inf.readline().strip()
num = ''
for i in range(len(s)):
    if s[i].isalpha():
        ch = s[i]
    else:
        num += s[i]
    if i == len(s) - 1 or s[i + 1].isalpha():
        print(ch * int(num), end='')
        num = ''
