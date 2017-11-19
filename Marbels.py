# your code goes here# your code goes here
def fact(case):
    if case==0:
        return 1
    elif case==1:
        return 1
    else:
        return case*fact(case-1)
        
def calculate(n, k):
    a=n-1
    b=k-1
    c=n-k
    i=max(b,c)
    afact=1
    while i<a:
        afact*=i+1
        i+=1
        
    result += afact//fact(min(b,c))
    print(result)
       
def main():
    noOfCases=int(input())
    for i in range(noOfCases):
        n, k = map(int, input().split())
        calculate(n, k)
main()