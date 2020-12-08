with open("AoC8.txt", 'r') as File1:
    info = []
    for line in File1:
        info.append(line.split("\n")[0])
jmp_loc = []
nop_loc = []
history = []
for l in range(len(info)):
    if "jmp" in info[l]:
        jmp_loc.append(l)
    elif "nop" in info[l]:
        nop_loc.append(l)
for jmp in jmp_loc:
    visited = []
    accumulator = 0
    i = 0
    tmp_info = []
    for k in range(len(info)):
        if k == jmp:
            tmp_info.append(f"nop {info[k].split(' ')[1]}")
        else:
            tmp_info.append(info[k])
    while True:
        try:
            if tmp_info[i].split(" ")[0] == "acc":
                if i not in visited:
                    accumulator += int(tmp_info[i].split(" ")[1])
                    visited.append(i)
                    i += 1
                else:
                    break
            elif tmp_info[i].split(" ")[0] == "jmp":
                if i + int(tmp_info[i].split(" ")[1]) not in visited:
                    visited.append(i)
                    i += int(tmp_info[i].split(" ")[1])
                else:
                    break
            else:
                visited.append(i)
                i += 1
        except IndexError:
            print(jmp)
            break
    history.append([accumulator, visited])

for nop in nop_loc:
    visited = []
    accumulator = 0
    i = 0
    tmp_info = []
    for k in range(len(info)):
        if k == nop:
            tmp_info.append(f"jmp {info[k].split(' ')[1]}")
        else:
            tmp_info.append(info[k])
    while True:
        try:
            if tmp_info[i].split(" ")[0] == "acc":
                if i not in visited:
                    accumulator += int(tmp_info[i].split(" ")[1])
                    visited.append(i)
                    i += 1
                else:
                    break
            elif tmp_info[i].split(" ")[0] == "jmp":
                if i + int(tmp_info[i].split(" ")[1]) not in visited:
                    visited.append(i)
                    i += int(tmp_info[i].split(" ")[1])
                else:
                    break
            else:
                visited.append(i)
                i += 1
        except IndexError:
            break
    history.append([accumulator, visited])

for thing in history:
    thing[1].sort()
    if thing[1][-1] == len(info):
        print(thing)
