with open("AoC6.txt", 'r') as File1:
    info = []
    newline = "\n"
    for line in File1:
        if line == "\n":
            info.append("\n\n")
        else:
            info.append(f'''{line.split(newline)[0]}\n''')
customs = []
customs = "".join(info).split("\n\n")

for i in range(len(customs)):
    customs[i] = customs[i].split("\n")
    if customs[i][0] == "":
        customs[i].remove("")

answers = []

for group in customs:
    answered = []
    count = 0
    for answer in group:
        for question in answer:
            if question not in answered:
                answered.append(question)
                count += 1
    answers.append(count)
#  print(answers)
print(sum(answers))
