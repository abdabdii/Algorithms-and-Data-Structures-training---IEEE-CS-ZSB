stones = input().lstrip().rstrip()
instructions = input().lstrip().rstrip()

currentPos = 1
for instruction in instructions:
    if instruction == stones[currentPos-1]:
        currentPos += 1

print(currentPos)
