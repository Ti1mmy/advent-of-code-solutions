from math import ceil
with open("AoC5.txt", 'r') as File1:
    info = []
    for line in File1:
        info.append(line.split("\n")[0])
highest = 0


def parse_row(f_b):
    if f_b == "B":
        return row_n[ceil((len(row_n) / 2))::]
    else:
        return row_n[0:ceil((len(row_n) / 2))]


def parse_column(l_r):
    if l_r == "R":
        return column_n[(len(column_n) // 2)::]
    else:
        return column_n[0:(len(column_n) // 2)]


for boarding in info:
    row = boarding[0:7]
    column = boarding[7::]
    # print(row, column)
    row_n = [n for n in range(128)]
    column_n = [n for n in range(8)]
    for fb in row:
        row_n = parse_row(fb)
        # print(temp)
    for lr in column:
        column_n = parse_column(lr)
        # print(temp)
    if int(row_n[0]) * 8 + int(column_n[0]) > highest:
        highest = int(row_n[0]) * 8 + int(column_n[0])
print(highest)
