TestCase = int(input())
while TestCase > 0:
    Number = int(input())
    while(Number > 0):
        fact = fact * Number
        Number = Number - 1
    print(fact)
    TestCase = TestCase - 1
