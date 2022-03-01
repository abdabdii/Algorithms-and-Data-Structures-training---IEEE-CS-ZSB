nXm = input().lstrip().rstrip()
matrix = []
for _ in range(int(nXm[0])):
    strings = input().lstrip().rstrip()
    string_list = list(map(str, strings.split()))
    matrix.append(string_list)
isColored = False
colord = ["C", "M", "Y"]
for row in matrix:
    if any(x in colord for x in row):
        isColored = True
        break
if isColored:
    print("#Color")
else:
    print("#Black&White")
