n = int(input())
Player1 = []
Player2 = []
max1 = int(0)
max2 = int(0)
count1 = int(0)
count2 = int(0)
for i in range(0,n):
    Score1, Score2 = input().split()
    count1 += int(Score1)
    count2 += int(Score2)
    if count1 > count2:
        if max1 < (count1 - count2):
            max1 = count1 - count2
        p = 1
    else:
        if max1 < (count2 - count1):
            max1 = count2 - count1
        p = 2
print(p,max1)


