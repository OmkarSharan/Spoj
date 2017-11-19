from sys import stdin
tc = int(stdin.readline().rstrip())
s = 1
while tc:
    tc -= 1
    stamp, frnd = map(int,stdin.readline().rstrip().split())
    lst = []
    lst = list(map(int, stdin.readline().rstrip().split()))
    lst.sort()
    lst.reverse()
    sum = 0
    count = 0
    for i in lst:
        sum += i
        count += 1
        if sum >= stamp:
            break
    print("Scenario #%s:" %(s))
    if sum >= stamp:
        print(count)
    else:
        print("impossible")
    print()
    s += 1
