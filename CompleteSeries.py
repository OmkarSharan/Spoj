import math
t = int(input())
while t:
    third, lthird, sum = map(int, input().split())
    n = (2 * sum) // (third + lthird)
    cd = (lthird - third) // (n - 5)
    a = third - 2 * cd
    print(n)
    for i in range(0, n - 1):
        print(a + (i * cd), end=" ")
    print(a + (n - 1)* cd, end="\n")
    t -= 1