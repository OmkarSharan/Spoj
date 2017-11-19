from sys import stdin, stdout

def knapsack(wt, fun, budget, n):
    if n == 0 or budget == 0:
        return 0
    if wt[n - 1] > budget:
        return knapsack(wt, fun, budget, n - 1)
    else:
        return max(wt[n - 1] + knapsack(wt, fun, budget - wt[n - 1], n - 1), knapsack(wt, fun, budget, n - 1))

budget, n = map(int, stdin.readline().split())
wt = [] * n
fun = [] * n
while True:
    if budget == 0 and n == 0:
        break
    else:
        for i in range(n):
            x, y = map(int, stdin.readline().split())
            wt.append(x)
            fun.append(y)
    print(knapsack(wt, fun, budget, n))
    print()
    budget, n = map(int, stdin.readline().split())

