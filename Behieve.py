from sys import stdin, stdout
import math
while True:
    n = int(stdin.readline().rstrip())
    if n == -1:
        break
    p = math.sqrt((4 * n - 1)/3)
    q = int(math.sqrt((4 * n - 1) / 3))
    if p * p == q * q:
        stdout.write("Y" + "\n")
    else:
        stdout.write("N" + "\n")

