#!/usr/bin/env python3

mass = input().split()

for i in mass:
    mass2 = list(i)
    for a in range(len(mass2)):
        ch = mass2[a]
        if ch.isalpha():
            if ord(ch) > 120:
                ch = chr(ord(ch) - 26)
            mass2[a] = chr(ord(ch) + 2)
    print(''.join(mass2), end=' ')
