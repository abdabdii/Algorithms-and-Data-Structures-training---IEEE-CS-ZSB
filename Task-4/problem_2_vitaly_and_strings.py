s = input()
t = input()
sList = list(s)


def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65)


for i, e in reversed(list(enumerate(sList))):
    if e == 'z':
        sList[i] = 'a'
    else:
        sList[i] = next_alpha(e).lower()
        break

s = ''.join(sList)
if s < t:
    print(s)
else:
    print("No such string")
