with open("AoC8.txt", 'r') as File1:
    info = []
    for line in File1:
        info.append(line.split("\n")[0])
visited = []
accumulator = 0
i = 0

while True:
    if info[i].split(" ")[0] == "acc":
        if i not in visited:
            accumulator += int(info[i].split(" ")[1])
            visited.append(i)
            i += 1
        else:
            break
    elif info[i].split(" ")[0] == "jmp":
        if i + int(info[i].split(" ")[1]) not in visited:
            visited.append(i)
            i += int(info[i].split(" ")[1])
        else:
            break
    else:
        visited.append(i)
        i += 1

print(accumulator)
