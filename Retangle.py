from sys import stdin
import math
n = int(stdin.readline().rstrip())
count = 0
for i in range(1, int(math.sqrt(n)) + 1):
    count += (n // i - i + 1)
print(count)