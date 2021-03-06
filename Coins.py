# your code goes here
import fileinput
 
max_values = {}
 
def solve(n):
    sol = n
    
    if n in max_values:
        sol = max_values[n]
    else:
        if not n == 0:
            coin1 = solve(int(n/2))
            coin2 = solve(int(n/3))
            coin3 = solve(int(n/4))
            
            sol = max(n, coin1 + coin2 + coin3)
            max_values[n] = sol
    
    return sol
        
 
for line in fileinput.input():
    n = int(line)
    result = solve(n)
    print(result) 