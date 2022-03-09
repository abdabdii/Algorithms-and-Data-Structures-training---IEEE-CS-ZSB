from math import floor
from decimal import Decimal

inputString = input().split()
n = int(inputString[0])
m = int(inputString[1])
k = Decimal(inputString[2])

skills = []
tracked = []
for _ in range(0, m+n):
    skill = input().split(" ")
    if len(skill) == 2:
        skill[1] = int(skill[1])
        level = floor(skill[1]*k)
        if level >= 100:
            skills.append({"name": skill[0], "level": level})
            tracked.append(skill[0])
    else:
        if skill[0] not in tracked:
            skills.append({"name": skill[0], "level": 0})

skills = sorted(skills, key=lambda x: x["name"], reverse=False)
print(len(skills))
for skill in skills:
    print(skill["name"] + " " + str(skill["level"]))
