number = int(input())
currentMultiplier = 1
while currentMultiplier <= 10:
    statement = str(currentMultiplier) + " x " + \
        str(number) + " = " + str(number*currentMultiplier)
    print(statement)
    currentMultiplier += 1
