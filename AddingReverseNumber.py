t = int(input())
while t:
    string = input().split()
    str1 = ''.join(reversed(string[0]))
    str2 = ''.join(reversed(string[1]))
    str3 = str(int(str1) + int(str2))
    print(int(''.join(reversed(str3))))
    t -= 1
