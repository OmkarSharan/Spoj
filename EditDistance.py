from sys import stdin, stdout
matrix = [[0 for i in range(2005)] for j in range(2005)]
def editDistance(str1, str2, l1, l2):
    for i in range(l1 + 1):
        matrix[0][i] = i
    for i in range(l2 + 1):
        matrix[i][0] = i
    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            if str2[i - 1] == str1[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
    return matrix[l2][l1]

tc = int(stdin.readline().rstrip())
while tc:
    tc -= 1
    str1 = stdin.readline().rstrip()
    str2 = stdin.readline().rstrip()
    l1 = len(str1)
    l2 = len(str2)
    stdout.write(str(editDistance(str1, str2, l1, l2))+"\n")


