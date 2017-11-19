def mergSort(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right ) // 2
        count = mergSort(arr, left, mid)
        count += mergSort(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    return count

def merge(arr,l, m, r):
    tmp = [0] * (r + l + 1)
    i = l; j = m + 1 ; k = l
    invr_count = 0
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1; k += 1
        else:
            tmp[k] = arr[j]
            j += 1; k += 1
            invr_count += (m - i)
    while i <= m:
        tmp[k] = arr[i]
        i += 1; k += 1
    while j <= r:
        tmp[k] = arr[j]
        j += 1; k += 1
    for i in range(l, k):
        arr[i] = tmp[i]
    return invr_count

tc = int(input())
while tc:
    input()
    tc -= 1
    n = int(input())
    arr = []
    for i in range(0, n):
        x = int(input())
        arr.append(x)
    print(mergSort(arr, 0, len(arr) - 1))




