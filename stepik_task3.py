math = 0
phys = 0
rus = 0
count = 0
with open('my_2.txt') as file, open('out.txt', 'w') as ouf:
    for string in file:
        lst = string.strip().split(';')
        ouf.write(str(sum([int(lst[1]), int(lst[2]), int(lst[3])]) / 3) + '\n')
        math += int(lst[1])
        phys += int(lst[2])
        rus += int(lst[3])
        count += 1
    ouf.write(str(math / count) + " " + str(phys / count) +
              " " + str(rus / count))
