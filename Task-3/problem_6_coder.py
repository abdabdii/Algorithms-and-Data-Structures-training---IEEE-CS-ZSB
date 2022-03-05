players = int(input().lstrip().rstrip())

numOfCoders = 0
skipOrNoSkipX = False
skipOrNoSkipY = False
result = []
for i in range(0, players):
    skipOrNoSkipX = skipOrNoSkipY
    row = ["."]*players
    for idx, letter in enumerate(row):
        if not skipOrNoSkipX:
            letter = "C"
            numOfCoders += 1
        skipOrNoSkipX = not skipOrNoSkipX
        result.append(letter)
    skipOrNoSkipY = not skipOrNoSkipY
    result.append("\n")

print(numOfCoders)
print("".join(result))
