column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

diffcolumn = abs(column1 - column2)
diffrow = abs(row1 - row2)

if diffcolumn <= 1 and diffrow <= 1:
    print("YES")
else:
    print("NO")
