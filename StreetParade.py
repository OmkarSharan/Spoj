while True:
    n = int(input())
    if n == 0:
        break
    arr = [0] * n
    stck = [0] * n
    i = 0
    k = 0
    top = -1
    arr = [int(i) for i in input().split()]  # arr = list(map(int, input().split()))
    while arr[i] != 1:
        top += 1
        stck[top] = arr[i]
        i += 1
    count = 1
    while True:
        if i < n and count == arr[i]:
            if i < n:
                i += 1
            count += 1
        elif top >= 0 and count == stck[top]:
            count += 1
            if top >= 0:
                top -= 1
        elif i < n and count != arr[i]:
            top += 1
            stck[top] = arr[i]
            if i < n:
                i += 1
        else:
            break
    if count == n + 1:
        print("yes")
    else:
        print("no")
