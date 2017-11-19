from sys import stdin

n = int(stdin.readline().rstrip())

if n <= 1 or (n & n-1) == 0:
    print("TAK")
else:
    print("NIE")