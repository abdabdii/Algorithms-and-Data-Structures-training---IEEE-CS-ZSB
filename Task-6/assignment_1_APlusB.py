integers_string = input().lstrip().rstrip()
integers_list = list(map(int, integers_string.split()))
print(integers_list[0]+integers_list[1])