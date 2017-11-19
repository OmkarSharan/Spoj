import sys

f = open("file.txt","r")
for line in f:
    print(line.strip())
    break
f.close()