from math import log, ceil
t = int(input())
i = 1
while t:
    t -= 1
    a, b, c = map(int, input().split())
    x = ceil(log(a, 2)) + ceil(log(b, 2)) + ceil(log(c, 2))
    print("Case #%d: %d %d" %(i, a * b * c - 1, int(x)))
    i += 1