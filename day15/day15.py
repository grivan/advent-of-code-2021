from copy import copy
import sys

sys.setrecursionlimit(2000)


INPUT = "day15/day15_sample.in"

# f(n,n) = min(f(n-1, n), f(n, n-1), f(n+1,n), f(n,n+1)) + cost(n,n)

def cost(x, y):
    if totals[x][y] != None:
        return totals[x][y]
    
    ccost = None
    if x < 0 or y < 0 or x >= l or y >= l:
        return 1000000
    elif x == 0 and y == 0:
        ccost = 0
    else:
        ccost = min(cost(x-1, y), cost(x, y-1)) + costs[x][y]
    
    totals[x][y] = ccost
    return ccost

with open(INPUT) as infile:
    costs = [[int(x) for x in line.rstrip()] for line in infile]
    l = len(costs)
    totals = [[None for _ in range(l)] for _ in range(l)]
    print("PART 1: " + str(cost(l-1, l-1)))
    
    ll = 5*l
    lcosts = [[None for _ in range(ll)] for _ in range(ll)]
    for i in range(ll):
        for j in range(ll):
            ci, cj = i % l, j % l
            plus = int(i / l) + int(j / l)
            c = costs[ci][cj]
            for _ in range(plus):
                c+=1
                if c > 9:
                    c = 1
            lcosts[i][j] = c
    
    # print("\n".join([ "".join([str(x) for x in line]) for line in lcosts]))
    
    costs = lcosts
    totals = [[None for _ in range(ll)] for _ in range(ll)]
    l = ll
    print("PART 2: " + str(cost(ll-1, ll-1)))