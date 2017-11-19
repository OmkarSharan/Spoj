while True:

    output={}
    n= int(input())
    if n==0: break
    caseList= list(map(int, input().split()))
    for i in range(0, n):
        output[caseList[i] - 1] = i + 1
    for i in range(0, n):
        if output[i] != caseList[i]:
            break

    if i == n - 1:
        print("ambiguous")
    else:
        print("not ambiguous")