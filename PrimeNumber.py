import math
t = int(input())
for i in range(0, t):
    def primeNumber(n):
        if n == 0 or n == 1:
            return False
        elif n == 2 or n == 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            flag = False
            for i in range(3, int(math.sqrt(n))+2):
                if i != n and n % i == 0:
                    flag = False
                    break
                else:
                    flag = True
            return flag


    n = int(input())
    P = primeNumber(n)
    if P:
        print("prime")
    else:
        print("Not prime")