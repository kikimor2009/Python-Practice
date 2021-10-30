column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

diffcolumn = column1 - column2
diffrow = row1 - row2

if diffcolumn == 0 or diffrow == 0:
    print("YES")
else:
    print("NO")
