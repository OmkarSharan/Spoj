from sys import stdin

while True:
    string = stdin.readline().rstrip()
    if string[0] == '0':
        break
    arr = {}
    arr[0] = 1
    arr[1] = 1
    for i in range(2, len(string) + 1):
        arr[i] = 0
        c1 = int(str(string[i - 2]))
        c2 = int(str(string[i - 1]))
        if c1 == 1 or c1 == 2 and c2 <= 6:
            arr[i] += arr[i - 2]
        if c2!= 0:
            arr[i] += arr[i - 1]
    print(arr[len(string)])
