from sys import stdin, stdout
a, n, k = map(int, stdin.readline().rstrip().split())

for i in range(0, k):
    if a == 0:
        print(0, end=" ")
    else:
        print(a % (n + 1), end=" ")
        a //= (n + 1)