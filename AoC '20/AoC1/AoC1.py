info = []
with open("AoC1.txt", 'r') as File1:
    for line in File1:
        info.append(int(line))
info.sort()
print(info)
for cost1 in info:
    for cost2 in info:
        for cost3 in info:
            if cost1 + cost2 + cost3 == 2020:
                print(cost1 * cost2 * cost3)
