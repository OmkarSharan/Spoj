TestCase = int(input())
while TestCase > 0:
    Number = int(input())
    fact = 1;
    while(Number > 0):
        fact = fact * Number
        Number = Number - 1
    print(fact)
    TestCase = TestCase - 1
