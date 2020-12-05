info = []
with open("AoC2.txt", 'r') as File1:
    for line in File1:
        info.append([int(line[:-1].split("-")[0]),
                    int(line[:-1].split(" ")[0].split("-")[1]),
                    line[:-1].split(":")[0][-1],
                    line[:-1].split(" ")[-1]])
i = 0
print(info)
for password in info:
    try:
        if password[3][password[0] - 1] == password[2] and password[3][password[1] - 1] == password[2]:
            pass
        elif password[3][password[0] - 1] == password[2] or password[3][password[1] - 1] == password[2]:
            i += 1
    except IndexError:
        pass
print(i)