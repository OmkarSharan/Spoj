arr = [0] * 100
arr[0] = 1
arr[1] = 3
for i in range(2, 100):
    arr[i] = 2 * arr[i - 1] + arr[i - 2]
n = int(input())
print(arr[n])
