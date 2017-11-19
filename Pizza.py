from sys import stdin, stdout
from math import ceil
frnds = int(stdin.readline())
half = 0
oneforth = 0
threeforth = 0
for i in range(frnds):
    str = stdin.readline()
    if str[0] == '1' and str[2] == '2':
        half += 1
    if str[0] =='1' and str[2] == '4':
        oneforth += 1
    if str[0] =='3' and str[2] =='4':
        threeforth += 1
if half % 2 == 0:
    extraonefoth = threeforth
else:
    extraonefoth = 2 + threeforth
    half += 1
if oneforth <= extraonefoth:
    print(1 + threeforth + half // 2)
else:
    print(1 + threeforth + half // 2 + ceil((oneforth - extraonefoth) / 4))