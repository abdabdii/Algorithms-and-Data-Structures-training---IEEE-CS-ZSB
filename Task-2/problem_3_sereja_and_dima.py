sizeOfArray = int(input())
integers_string = input().lstrip().rstrip()
integers_list = list(map(int, integers_string.split()))

Spoints = 0
Dpoints = 0
i = 0


def addPoints(i, Spoints, Dpoints, points):
    if i % 2 == 0:
        Spoints += points
    else:
        Dpoints += points
    return Spoints, Dpoints


while len(integers_list) != 0:
    points = 0
    if integers_list[-1] >= integers_list[0]:
        points = integers_list.pop(-1)
    else:
        points = integers_list.pop(0)
    Spoints, Dpoints = addPoints(i, Spoints, Dpoints, points)
    i += 1

print(str(Spoints) + " " + str(Dpoints))
