a, b = map(int, input().split())
diff = a - b
if diff % 10 == 9:
    ans = diff - 1
else:
    ans = diff + 1
print(ans)
