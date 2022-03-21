arrLength = input().lstrip().rstrip()
integers_string = input().lstrip().rstrip()
integers_list = list(map(int, integers_string.split()))

max1 = max(integers_list)
if integers_list.count(max1) > 1:
    print(max1*max1)
else:
    integers_list.remove(max1)
    print(max1*max(integers_list))
2