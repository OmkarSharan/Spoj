from sys import stdin, stdout

tc = int(stdin.readline())
while tc:
    tc -= 1
    n, player = map(int, stdin.readline().split())
    if n == 1:
        if player == 0:
            print("Airborne wins.")
        if player == 1:
            print("Pagfloyd wins.")
    else:
        if player == 1:
            print("Pagfloyd wins.")
        else:
            print("Airborne wins.")