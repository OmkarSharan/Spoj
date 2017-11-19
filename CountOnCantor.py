from sys import stdin

t = int(stdin.readline().rstrip())
while t:
    n = int(stdin.readline().rstrip())
    count = 0
    i = 1
    j = 1
    count += 1
    while count < n:
        j += 1
        count += 1
        if count == n:
            break
        while j > 1:
            i += 1
            j -= 1
            count += 1
            if count == n:
                break
        if count == n:
            break
        i += 1
        count += 1
        if count == n:
            break
        while i > 1:
            j += 1
            i -= 1
            count += 1
            if count == n:
                break
        if count == n:
            break
    print('TERM %d IS %d/%d'%(n, i, j))
    t -= 1
