t = int(input())
while t:
    t -= 1
    input()
    n = int(input())
    sum = 0
    for i in range(0, n):
        x = int(input())
        sum += x
    if sum % n == 0:
        print("YES")
    else:
        print("NO")
