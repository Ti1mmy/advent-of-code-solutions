newline = "\n"
with open("AoC6.txt", 'r') as File1:
    info = []
    for line in File1:
        if line == "\n":
            info.append("\n\n")
        else:
            info.append(f'''{line.split(newline)[0]}\n''')
#  print(info)
customs = []
customs = "".join(info).split("\n\n")
#  print(customs)
for i in range(len(customs)):
    customs[i] = customs[i].split("\n")
    try:
        customs[i].remove('')
    except ValueError:
        pass
answers = []
#  print(customs)
for group in customs:
    answered = {}
    count = 0
    occurrences = 0
    for answer in group:
        for question in answer:
            if question not in answered:
                answered[question] = 1
            else:
                answered[question] += 1
    for key, value in answered.items():
        #  print(group)
        if answered[key] == len(group):
            count += 1
    #  print(answered)
    answers.append(count)
#  print(answers)
print(sum(answers))
