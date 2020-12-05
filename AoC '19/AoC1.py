import sys
input = sys.stdin.readline
sum = 0
while True:
    a = input()
    if a == "\n":
        break
    else:
        b = int(a)
        while (b // 3) - 2 > 0:
            b = (b // 3) - 2
            sum += b
print(sum)