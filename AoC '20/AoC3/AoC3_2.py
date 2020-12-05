info = []
with open("AoC3.txt", 'r') as File1:
    for line in File1:
        info.append((line.split("\n")[0]) * 1000)
all_trees = []


def sled(right, down):
    trees_t = 0
    i_t = 0
    for k in range(0, len(info), down):
        if info[k][i_t] == "#":
            trees_t += 1
        i_t += right
    return trees_t


all_trees = [
        sled(1, 1),
        sled(3, 1),
        sled(5, 1),
        sled(7, 1),
        sled(1, 2)
    ]
output = 1
print(all_trees)
for tree in all_trees:
    output *= tree
print(output)