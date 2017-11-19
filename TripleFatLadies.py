from sys import stdin

t = int(stdin.readline().rstrip())
while t:
    p = 192
    k = int(stdin.readline().rstrip())
    if k == 1:
        print(p)
    else:
        print(p + 250 * (k - 1))

    t -= 1
