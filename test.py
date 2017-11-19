from sys import stdin, stdout
n, m, a = map(int, stdin.readline().rstrip().split())

h = n//a
if n%a != 0: h+=1

w = m//a
if m%a != 0: w+=1

stdout.write( str(h*w) + "\n" )

