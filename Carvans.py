from sys import stdin
t = int(stdin.readline().rstrip())
while t:
    n = int(stdin.readline().rstrip())
    arr = []
    count = 1
    arr = [int(i) for i in input().split()]
    min = arr[0]
    for i in range(1, n):
            if arr[i] <= min:
                min = arr[i]
                count += 1
    print(count)
    t -= 1
