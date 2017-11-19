

from sys import stdin, stdout
tc = int(stdin.readline().rstrip())
while tc:
    tc -= 1
    str1 = stdin.readline().rstrip()
    str2 = stdin.readline().rstrip()
    print(edit_distance(str1, str2))
