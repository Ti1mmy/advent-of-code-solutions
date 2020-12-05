info = []
contents = ""
with open("AoC4.txt", "r") as File1:
    for line in File1:
        contents += line
    info = contents.split("\n\n")
valid = 0
for thing in info:
    thing2 = thing.replace("\n", " ")
    temp = thing2.split(" ")
    #  print(temp)
    temp.sort()
    validb = 0
    thing = "".join(temp)
    if "byr" in thing and \
            "iyr" in thing and \
            "eyr" in thing and \
            "hgt" in thing and \
            "hcl" in thing and \
            "ecl" in thing and \
            "pid" in thing:
        for thing in temp:
            if "byr" in thing:
                if 1920 <= int(thing.split(":")[1]) <= 2002:
                    validb += 1
            elif "ecl" in thing:
                if "amb" == thing.split(":")[1] or \
                        "blu" == thing.split(":")[1] or \
                        "brn" == thing.split(":")[1] or \
                        "gry" == thing.split(":")[1] or \
                        "grn" == thing.split(":")[1] or \
                        "hzl" == thing.split(":")[1] or \
                        "oth" == thing.split(":")[1]:
                    validb += 1
            elif "eyr" in thing:
                if 2020 <= int(thing.split(":")[1]) <= 2030:
                    validb += 1
            elif "hcl" in thing:
                if thing.split(":")[1][0] == "#":
                    if len(thing.split(":")[1]) == 7:
                        if (char in "0123456789abcdef" for char in thing.split(":")[1][1::]):
                            validb += 1
            elif "hgt" in thing:
                if thing[-2:] == "cm":
                    if 150 <= int((thing.split(":")[1].split("cm")[0])) <= 193:
                        validb += 1
                        #  print(f'Valid Height: {int((thing.split(":")[1].split("cm")[0]))}cm')
                elif thing[-2:] == "in":
                    if 59 <= int((thing.split(":")[1].split("in")[0])) <= 76:
                        validb += 1
                        #  print(f'Valid Height: {int(thing.split(":")[1].split("in")[0])}in')
            elif "iyr" in thing:
                if 2010 <= int(thing.split(":")[1]) <= 2020:
                    validb += 1
                    #  print(f'Valid byr: {int(thing.split(":")[1])}')
            elif "pid" in thing:
                try:
                    if len(thing.split(":")[1]) == 9:
                        #  print(f'Valid pid: {int(thing.split(":")[1])}')
                        validb += 1
                except TypeError:
                    pass
                except ValueError:
                    pass
            #  print(validb)
            if validb == 7:
                valid += 1
print(f"Total valid: {valid}")
