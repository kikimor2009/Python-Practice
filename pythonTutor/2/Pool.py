n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    long = n
    short = m
else:
    long = m
    short = n

if x * 2 > short:
    x = short - x
if y * 2 > long:
    y = long - y

print(min(x, y))
