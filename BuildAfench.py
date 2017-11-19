while True:
    l = int(input())
    if l == 0:
        break
    pi = 3.1415926
    area = float(l * l / float(2 * pi))
    print("%.2f" %(area))