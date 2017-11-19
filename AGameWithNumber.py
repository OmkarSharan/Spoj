n = int(input())
if n <= 9:
    print("1")
    print(n)
elif n % 10 != 0:
    print("1")
    print(n % 10)
else:
    print("2")