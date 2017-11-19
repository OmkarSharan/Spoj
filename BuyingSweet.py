from sys import stdin


def subsetsum(arr, sum, n):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n - 1] > sum:
        return subsetsum(arr, sum, n - 1)
    else:
        return subsetsum(arr, sum, n - 1) or subsetsum(arr, sum - arr[n - 1], n - 1)


t = int(stdin.readline().rstrip())
while t:
    n, p = map(int, stdin.readline().rstrip().split())
    arr = []
    arr = [int(i) for i in input().split()]
    total = sum(arr)
    if total % p == 0:
        print(sum // p)
    elif total % p != 0:
        if n == 1 and total >= p:
            print("1")
        else:
            temp = total - total % p
            if subsetsum(arr, temp, n):
                print(total // p)
            else:
                print("-1")
    t -= 1
