import re
path = input()
path = re.sub(r"(/+)", r"/", path)
if path[-1] == '/' and len(path) > 1:
    path = path[:-1]
print(path)
