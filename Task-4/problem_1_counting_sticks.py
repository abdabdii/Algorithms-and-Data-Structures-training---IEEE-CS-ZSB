import math as m

s = input().split("=")
equation = s[0].split("+")
a = len(equation[0])
b = len(equation[1])
result = len(s[1])

if a+b+result % 2 == 1:
    print("Impossible")
elif m.fabs(result-a-b) != 2 and a+b != result:
    print("Impossible")
elif a+b == result:
    print(a*"|", "+", b*"|", "=", result*"|", sep="")
elif result-a-b == 2:
    result -= 1
    b += 1
    print(a*"|", "+", b*"|", "=", result*"|", sep="")
elif result-a-b == -2:
    result += 1
    if b > 1:
        b -= 1
    else:
        a -= 1
    print(a*"|", "+", b*"|", "=", result*"|", sep="")
