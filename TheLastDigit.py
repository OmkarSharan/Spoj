from sys import stdin
t = int(stdin.readline().rstrip())

while t:
    a, b = map(int, stdin.readline().rstrip().split())
    a %= 10
    if a == 0:
        print(0)
    elif b == 0:
        print(1)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        p = b % 4
        if p == 0:
            p = 4
        print(a ** p % 10)
    elif a == 4 or a == 9:
        p = b % 2
        if p == 0:
            p = 2
        print(a ** p % 10)
    elif a== 1 or a == 5 or a == 6:
        print(a)
    t -= 1
