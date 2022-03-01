import math
nAndK = list(map(int, input().lstrip().rstrip().split()))
contestsList = list(map(int, input().lstrip().rstrip().split()))

i = 0
while i < nAndK[0]:
    if contestsList[-1] <= nAndK[1]:
        contestsList.pop()
    if len(contestsList) > 0:
        if contestsList[0] <= nAndK[1]:
            contestsList.pop(0)
    i += 1
    if len(contestsList) == 0:
        break

print(nAndK[0] - len(contestsList))
