rows = int(input().lstrip().rstrip())
rowsList = []
found = False
for _ in range(rows):
    rowStr = input().lstrip().rstrip()
    seats = rowStr.split("|")
    if not found:
        if seats[0] == "OO":
            rowStr = "++"+"|"+seats[1]
            found = True
        elif seats[1] == "OO":
            rowStr = seats[0]+"|"+"++"
            found = True
    rowsList.append(rowStr)

if found:
    print("YES")
    print("\n". join(rowsList))
else:
    print("NO")
