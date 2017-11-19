import math

TestCase =int(input())
while TestCase > 0 :
    Number =int(input())
    flag = int(0)
    if Number == 0 or Number == 1:
        print("Not Prime")
    elif Number == 2 or Number == 3:
        print("Prime")
    elif Number % 2 == 0:
        print("Not Prime")
    else:
        for i in range(3,int(math.sqrt(Number))):
            if Number % i == 0:
                flag = 1
                break
        if flag == 1:
            print("Not Prime")
        else:
            print("Prime")
    TestCase = TestCase - 1