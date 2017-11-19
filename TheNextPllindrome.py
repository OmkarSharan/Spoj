from sys import stdin
t = int(stdin.readline().rstrip())

while t:
    n = int(stdin.readline().rstrip())
    n += 1
    while True:
        str1 = str(n)
        str2 = ''.join(reversed(str1))
        if str1 == str2:
            break
        n += 1
    print(n)
    t -= 1

