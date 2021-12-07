INPUT = "day7/day7.in"
    
with open(INPUT) as infile:
    
    positions = [int(pos) for pos in infile.readline().rstrip().split(',')]
    maxc = max(positions)
    minc = min(positions)
    
    costs = {}
    for i in range(minc, maxc):
        cost = 0
        for pos in positions:
            cost += (abs(pos-i) * (abs(pos-i) + 1)) / 2
        costs[i] = cost
    
    print(min(costs.values()))