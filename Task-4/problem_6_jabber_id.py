import re
stringInput = input()
regex = re.compile(
    r"^([0-9a-zA-Z_])+@([0-9a-zA-Z_]+\.)*([0-9a-zA-Z_])+(/([0-9a-zA-Z_])+)*$")

if regex.match(stringInput) is not None:
    print("YES")
else:
    print("NO")
