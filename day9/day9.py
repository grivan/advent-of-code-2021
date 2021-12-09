INPUT = "day9/day9.in"

with open(INPUT) as infile:
    heightmap = []
    
    for line in infile:
        heightmap.append([int(i) for i in (line.rstrip())])

    # PART 1
    lowest = []
    lowest_ids = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            cur = heightmap[i][j]
            neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            islowest = True
            for n in neighbors:
                try:
                    if n[0] < 0 or n[1] < 0:
                        continue
                    n_h = heightmap[n[0]][n[1]]
                    if n_h <= cur:
                        islowest = False
                except IndexError:
                    pass
        
            if islowest:
                lowest.append(cur+1)
                lowest_ids.append((i, j))
                
    print(sum(lowest))
    
    # PART 2
    # for each lowest point find the basin
    top_basins = []
    for low in lowest_ids:
        
        seen = set()
        stack = [low]
        size = 1
        
        while(len(stack) > 0):
            i, j = stack.pop()
            seen.add((i, j))
            curh = heightmap[i][j]
            
            neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            for n in neighbors:
                if n[0] < 0 or n[1] < 0 or n in seen:
                    continue
                try:
                    n_h = heightmap[n[0]][n[1]]
                    if n_h > curh and n_h != 9:
                        stack.append(n)
                except IndexError:
                    pass
        top_basins.append(len(seen))
        
    top_basins = sorted(top_basins)
    
    print(top_basins[-1] * top_basins[-2] * top_basins[-3])