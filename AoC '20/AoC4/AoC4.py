info = []
contents = ""
with open("AoC4.txt", "r") as File1:
    for line in File1:
        contents += line
    info = contents.split("\n\n")
valid = 0
for thing in info:
    if "byr" in thing and \
            "iyr" in thing and \
            "eyr" in thing and \
            "hgt" in thing and \
            "hcl" in thing and \
            "ecl" in thing and \
            "pid" in thing:
        valid += 1
print(valid)
