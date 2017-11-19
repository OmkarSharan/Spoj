n, k = input().split()
n = int(n)
k = int(k)
count = 0
for i in range(1,n + 1):
    t = int(input())
    if t % k == 0:
        count = count + 1;
print(count)

