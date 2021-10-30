def statistics(line):
    lst = line.split(";")
    if lst[0] not in d:
        d[lst[0]] = [0 for i in range(5)]
    if lst[2] not in d:
        d[lst[2]] = [0 for i in range(5)]

        if lst[1] > lst[3]:
            d[lst[0]][1] += 1
            d[lst[0]][4] += 3
            d[lst[2]][3] += 1
        elif lst[1] < lst[3]:
            d[lst[0]][3] += 1
            d[lst[2]][1] += 1
            d[lst[2]][4] += 3
        else:
            d[lst[0]][2] += 1
            d[lst[2]][2] += 1
            d[lst[0]][4] += 1
            d[lst[2]][4] += 1
        d[lst[0]][0] += 1
        d[lst[2]][0] += 1


d = {}

statistics("Зенит;3;Спартак;1")
statistics("Спартак;1;ЦСКА;1")
statistics("ЦСКА;0;Зенит;2")

for key in d:
    print(key, ":", sep='', end='')
    print(' '.join([str(i) for i in d[key]]))
