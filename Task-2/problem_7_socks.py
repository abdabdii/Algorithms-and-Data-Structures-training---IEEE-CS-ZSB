socksNumber = int(input().lstrip().rstrip())
socks = input().lstrip().rstrip()
socksList = list(map(int, socks.split()))
keysList = range(1, socksNumber+1)
wardrobe = dict.fromkeys(keysList, 0)
onTable = {"on": 0, max: 0}

for sock in socksList:
    wardrobe[sock] += 1
    if wardrobe[sock] != 2:
        onTable["on"] += 1

    else:
        if onTable["on"] > 0:
            onTable["on"] -= 1

    if onTable["on"] > onTable[max]:
        onTable[max] = onTable["on"]

print(onTable[max])
