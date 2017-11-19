import re
from sys import stdin, stdout
tc = int(stdin.readline())

while tc:
    tc -= 1
    n = int(stdin.readline())
    text = stdin.readline().strip()
    lst = {'HHH'}
    print(n, end=" ")
    for i in range(9):
        print(len(re.findall('(?=lst[0])', text)))

