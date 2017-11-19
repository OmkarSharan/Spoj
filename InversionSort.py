def mergSort(arr, tmp, left, right):
    count = 0
    if left < right:
        mid = (left + right ) // 2
        count = mergSort(arr, tmp, left, mid)
        count += mergSort(arr, tmp, mid + 1, right)
        count += merge(arr, tmp, left, mid, right)
    return count

def merge(arr, tmp, l, m, r):
    for i in range(l, r + 1):
        tmp[i] = arr[i]
    i = l; j = m + 1 ; k = l
    invr_count = 0
    while i <= m and j <= r:
        if tmp[i] < tmp[j]:
            arr[k] = tmp[i]
            i += 1; k += 1
        else:
            arr[k] = tmp[j]
            j += 1; k += 1
            invr_count += (m - i) + 1
    while i <= m:
        arr[k] = tmp[i]
        i += 1; k += 1
    while j <= r:
        arr[k] = tmp[j]
        j += 1; k += 1
    return invr_count

from sys import stdin
tc = int(stdin.readline())
while tc:
    input()
    tc -= 1
    n = int(stdin.readline())
    arr = []
    tmp = [0] * (n + 1)
    for i in range(0, n):
        x = int(input())
        arr.append(x)
    print(mergSort(arr, tmp, 0, len(arr) - 1))