from sys import stdin, stdout

tc = int(stdin.readline())
i = 0
while tc:
    i += 1
    rad = int(stdin.readline())
    print("Case %d: %.2f"%(i, 4 * rad * rad + 0.25))
    tc -= 1