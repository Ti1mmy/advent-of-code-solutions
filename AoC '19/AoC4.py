count = 0
double = False
passing = False
for i in range(int(input()), int(input())):
    numbers = [int(i) for i in str(i)]
    for i in range(1, 6):
        if i == 1:
            if numbers[i] == numbers[i - 1] and numbers[i] != numbers[i + 1]:
                double = True
                break
        elif i == 2 or i == 3 or i == 4:
            if numbers[i] == numbers[i - 1] and numbers[i] != numbers[i - 2] and numbers[i] != numbers[i+1]:
                double = True
                break
        else:
            if numbers[i] == numbers[i - 1] and numbers[i] != numbers[i - 2]:
                double = True
                break
    if numbers[0] <= numbers[1] <= numbers[2] <= numbers[3] <= numbers[4] <= numbers[5]:
        passing = True
    if passing and double:
        count += 1
    passing = False
    double = False
print(count)