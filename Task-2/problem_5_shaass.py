wires = input().lstrip().rstrip()
initialValues = input().lstrip().rstrip()
initialValuesList = list(map(int, initialValues.split()))
shots = int(input().lstrip().rstrip())
shotsList = []
for _ in range(shots):
    shotsStr = input().lstrip().rstrip()
    shotList = list(map(int, shotsStr.split()))
    shotsList.append(shotList)

for idx, shot in enumerate(shotsList):
    birdPosition = shot[1]
    wireNumber = shot[0] - 1
    rightBirds = initialValuesList[wireNumber]-birdPosition
    leftBirds = birdPosition-1
    initialValuesList[wireNumber] -= 1

    if wireNumber-1 >= 0:
        initialValuesList[wireNumber-1] += leftBirds
    if wireNumber+1 < int(wires):
        initialValuesList[wireNumber+1] += rightBirds
    initialValuesList[wireNumber] = 0

print(*initialValuesList, sep='\n')
