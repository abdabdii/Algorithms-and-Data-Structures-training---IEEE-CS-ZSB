inputList = input().split()
n = int(inputList[0])
p = int(inputList[1])
k = int(inputList[2])

result = []
if p-k > 1:
    result.append("<< ")
    for i in range(p-k, p):
        result.append(f"{i} ")
elif p-k <= 1:
    for i in range(1, p):
        result.append(f"{i} ")
result.append(f"({p}) ")

if p+k < n:
    for i in range(p+1, p+k+1):
        result.append(f"{i} ")
    result.append(">> ")
elif p+k >= n:
    for i in range(p+1, n+1):
        result.append(f"{i} ")

print("".join(result))
