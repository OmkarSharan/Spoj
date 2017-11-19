from sys import stdin

t = int(stdin.readline().rstrip())
while t:
    string = stdin.readline().rstrip()
    if len(string) % 2 != 0:
        firsthalf = string[:len(string) // 2]
        secondhalf = string[len(string) // 2 + 1:]
    else:
        firsthalf = string[:len(string) // 2]
        secondhalf = string[len(string) // 2:]
    firsthalf =''.join(sorted(firsthalf))
    secondhalf = ''.join(sorted(secondhalf))
    if firsthalf == secondhalf:
        print("YES")
    else:
        print("NO")

    t -= 1