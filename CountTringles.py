def linear_Sum(n):
    return (n * (n + 1))//2

t = int(input())
while t:
    t -= 1
    n = int(input())
    print((n * (2 * n + 1) * (n + 2))//8)