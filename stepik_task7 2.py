s1 = input()
s2 = input()
d1 = dict(zip(s1, s2))
d2 = dict(zip(s2, s1))

for ch in input():
    print(d1[ch], end='')
print()
for ch in input():
    print(d2[ch], end='')
