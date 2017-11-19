while True:
    g, b = map(int, input().split())
    if g == -1 and b == -1:
        break
    elif g == 0 and b == 0:
        ans = 0
    elif g >= b:
        b += 1
        ans = g // b
        if g % b:
            ans += 1
    else:
        g += 1
        ans = b // g
        if b % g:
            ans += 1
    print(ans)




