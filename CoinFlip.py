from sys import stdin, stdout
t = int(stdin.readline().rstrip())

while t:
    g = int(stdin.readline().rstrip())
    for i in range(0, g):
        I, n, q = map(int, stdin.readline().rstrip().split())
        if n % 2 == 0 and (q == 1 or q == 2):
            print(n // 2)
        elif n % 2 != 0 and I == 1 and q == 1:
            print(n // 2)
        elif n % 2 != 0 and I == 1 and q == 2:
            print(n // 2 + 1)
        elif n % 2 != 0 and I == 2 and q == 1:
            print(n // 2 + 1)
        elif n % 2 != 0 and I == 2 and q == 2:
            print(n // 2)

    t -= 1