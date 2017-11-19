tc = int(input())
mod = 1000007
for i in range(tc):
    n = int(input())
    ans = (3 * n * n + n)//2
    print(ans % mod)