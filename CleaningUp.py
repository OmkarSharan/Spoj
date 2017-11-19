from idlelib.MultiCall import r

t = int(input())
while t > 0:
    n, m = map(int, input().split())
    arr = [int(i) for i in range(0, n + 1)]
    A = []
    for i in input().split():
        A.append(int(i))
    for i in range(0, m):
        arr.remove(A[i])
    chef = []
    assistant = []
    i = 1
    while i < len(arr):
        chef.append(arr[i])
        i += 1
        if i < len(arr):
            assistant.append(arr[i])
        i += 1
    for i in range(0, len(chef)):
        print(chef[i], end= " ")
    print(end="\n")
    for i in range(0, len(assistant)):
        print(assistant[i], end=" ")
    print(end="\n")
    t -= 1
