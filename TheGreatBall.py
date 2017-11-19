t = int(input())
while t:
    t -= 1
    entry = []
    out = []
    n = int(input())
    for i in range(0, n):
        en, ex = map(int, input().split())
        entry.append(en)
        out.append(ex)
    entry.sort()
    out.sort()
    i = 0
    j = 0
    count = 0
    maximum = -1
    while i < n and j < n:
        if entry[i] <= out[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        if count > maximum:
            maximum = count
    print(maximum)
