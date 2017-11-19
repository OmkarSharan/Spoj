t = int(input())
while t:
    n = int(input())
    arr = []
    arr = [int(i) for i in input().split()]
    arr.sort(key = None, reverse = False)
    m = 9999999999
    for i in range(0, n):
        if i + 1 < n:
            minimum = abs(arr[i] - arr[i + 1])
            if m > minimum:
                m = minimum
    print(m)
    t -= 1