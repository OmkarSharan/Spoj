from sys import stdin, stdout
n = int(stdin.readline())
count = 0
while True:
    PowSum = 0
    while n > 0:
        PowSum += (n % 10) * (n % 10)
        n //= 10
    count += 1
    if PowSum == 1:
        break
    if count >= 9:
        break
    else:
        n = PowSum
if count >= 9:
    print("-1")
else:
    print(count)