INPUT = "day11/day11.in"
STEPS = 500

with open(INPUT) as infile:
    octo = []
    
    for line in infile:
        octo.append([int(i) for i in line.rstrip()])

    flashes = []
    for step in range(STEPS):
        
        flashing = []
        step_flash = 0
        
        # incremenet by 1
        for i in range(len(octo)):
            for j in range(len(octo[0])):
                octo[i][j]+=1
                if octo[i][j] > 9:
                    flashing.append((i, j))
        
        # flash!
        ns = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        flashed = set()
        loop = 0
        while(len(flashing) > 0):
            loop+=1
            i, j = flashing.pop()
            if (i,j) in flashed:
                continue
            
            # inc neighbors and update that flash
            for ni, nj in ns:
                l,m = i+ni, j+nj
                if l < 0 or m < 0 or l >= len(octo) or m >= len(octo[0]):
                    continue
                nvalue = octo[l][m] + 1
                if nvalue == 10:
                    flashing.append((l,m))
                octo[l][m] = nvalue
            
            flashed.add((i, j))
        
        # reset to 0, count flashes
        step_flash = 0
        for i in range(len(octo)):
            for j in range(len(octo[0])):
                if octo[i][j] > 9:
                    octo[i][j] = 0
                    step_flash+=1
    
        flashes.append(step_flash)
        
        if step == 100:
            print("Part 1 = ", sum(flashes))
            
        if step_flash == len(octo)*len(octo[0]):
            print("Part 2 = ", step+1)
            break