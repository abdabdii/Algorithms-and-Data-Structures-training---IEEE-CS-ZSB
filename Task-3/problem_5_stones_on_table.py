length = int(input().lstrip().rstrip())
letters = input().lstrip().rstrip()

numberToRemove = 0
for idx, letter in enumerate(letters):
    if idx < len(letters)-1 and letters[idx+1] == letter:
        numberToRemove += 1

print(numberToRemove)
