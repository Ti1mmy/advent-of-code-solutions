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
    occurences = 0
    for letter in password[3]:
        if password[2] == letter:
            occurences += 1
    if password[0] <= occurences <= password[1]:
        i += 1
print(i)