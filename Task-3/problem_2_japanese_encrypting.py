length = int(input().lstrip().rstrip())
row = (input().lstrip().rstrip()).split("W")

encryptedNubmer = 0
encryptionValues = []
for encoding in row:
    if encoding != "":
        encryptedNubmer += 1
        encryptionValues.append(str(len(encoding)))

print(encryptedNubmer)
print(" ". join(encryptionValues))
