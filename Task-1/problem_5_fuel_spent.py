hours = int(input())
speed = int(input())
liters = round(hours*speed/12, 3)
print(format(liters,'.3f'))
