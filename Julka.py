from sys import stdin
t = 10
while t:
    total = int(stdin.readline().rstrip())
    more = int(stdin.readline().rstrip())
    Kcludiya = (total + more) // 2
    Alka = total - Kcludiya
    print(Kcludiya)
    print(Alka)
    t -= 1