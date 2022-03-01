matrix = []
for i in range(0, 5):
    integers_string = input().lstrip().rstrip()
    integers_list = list(map(int, integers_string.split()))
    matrix.append(integers_list)
def search():
    for j in range(0, 5):
        for k in range(0, 5):
            if matrix[j][k] == 1:
                result = abs(2-k) + abs(2-j)
                print(result)
                break

search()
