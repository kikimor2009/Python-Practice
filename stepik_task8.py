def statistic(s):
    lst = s.split("\t")
    if int(lst[0]) not in d:
        d[int(lst[0])] = [0, 0]
    d[int(lst[0])][0] += 1
    d[int(lst[0])][1] += int(lst[2])


d = dict()

with open("file.txt") as inf:
    for line in inf:
        statistic(line)

for i in range(1, 12):
    if i not in d:
        print(str(i) + ' -')
    else:
        print(i, d[i][1] / d[i][0])
