length = int(input().lstrip().rstrip())
letters = input().lstrip().rstrip()

anton = 0
danik = 0
for letter in letters:
    if letter == "A":
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
