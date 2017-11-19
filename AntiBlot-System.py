from sys import stdin
t = int(input())
while t:
    input()
    string = stdin.readline().rstrip()
    i = 0
    j = 0
    k = 0
    str1 = []
    while string[i] != " ":
        str1.insert(i, string[i])
        i += 1
    str1 = ''.join(str1)
    i = i + 3
    str2 = []
    while string[i] != " ":
        str2.insert(j, string[i])
        j += 1
        i += 1
    str2 = ''.join(str2)
    i = i + 3
    str3 = []
    while i < len(string):
        str3.insert(k, string[i])
        k += 1
        i += 1
    str3 = ''.join(str3)
    p1 = 0
    p2 = 0
    p3 = 0
    if str1.isdigit():
        p1 = 1
    if str2.isdigit():
        p2 = 1
    if str3.isdigit():
        p3 = 1
    if p1 == 1 and p2 == 1:
        ans = int(str1) + int(str2)
        print(str1, "+", str2, "=", ans)
    if p1 == 1 and p3 == 1:
        ans = int(str3) - int(str1)
        print(str1, "+", ans, "=", str3,)
    if p2 == 1 and p3 == 1:
        ans = int(str3) - int(str2)
        print(ans, "+", str2, "=", str3)
    t -= 1