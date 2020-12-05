info = []
with open("AoC3.txt", 'r') as File1:
    for line in File1:
        info.append((line.split("\n")[0]) * 999)
i = 0
trees = 0
# length = len(info[0])
for k in range(len(info)):
    if info[k][i] == "#":
        trees += 1
    i += 1
print(trees)