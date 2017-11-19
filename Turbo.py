Aray = []
Number = int(input())
for i in range(0, Number):
    Elements = int(input())
    Aray.append(Elements)
Aray.sort(key = int)
for i in range(0, Number):
    print(Aray[i])

