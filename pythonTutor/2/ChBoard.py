column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

diffcolumn = abs(column1 - column2) % 2
diffrow = abs(row1 - row2) % 2

if (diffcolumn == 0 and diffrow == 0) or (diffcolumn != 0 and diffrow != 0):
    print("YES")
else:
    print("NO")
