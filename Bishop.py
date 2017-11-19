tc = 1024
while tc:
    tc -= 1
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print (n + n - 2)