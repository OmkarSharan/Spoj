def SubsetSum(arr, n, sum):
    if sum > 0 and n == 0:
        return False
    elif sum == 0:
        return True
    elif arr[n - 1] > sum:
        return SubsetSum(arr, n - 1, sum)
    else:
        return SubsetSum(arr, n - 1, sum) or SubsetSum(arr, n - 1, sum - arr[n - 1])


t = int(input())
while t:
    n, m = map(int, input().split())
    arr = []
    arr = [int(input()) for i in range(0, n)]
    if SubsetSum(arr, n, m):
        print("Yes")
    else:
        print("No")
    t -= 1
