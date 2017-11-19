from sys import stdin
t = int(stdin.readline().strip())
while t:
    j = stdin.readline().rstrip()
    s = stdin.readline().rstrip()
    count = 0
    for char in s:
        if char in j:
            count += 1;
    print(count)
    t -= 1