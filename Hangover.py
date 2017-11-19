from sys import stdin

while True:
    n = float(stdin.readline().rstrip())
    if n == 0.00:
        break;
    sum = 0.0
    count = 0
    i = 2
    while True:
        sum += 1 / i
        count += 1
        if sum >= n:
            break
        i += 1
    print(count, end="")
    print(" card(s)")
