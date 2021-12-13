INPUT = "day13/day13.in"

with open(INPUT) as infile:
    lines = infile.readlines()
    lines = [line.rstrip() for line in lines]
    
    folds = filter(lambda x: x.startswith('fold'), lines)
    folds = [(fold[11],int(fold[13:])) for fold in folds]
    
    coordinates = filter(lambda x: not x.startswith('fold') and len(x) > 0, lines)
    coordinates = [(int(c.split(',')[0]), int(c.split(',')[1])) for c in coordinates]
    
    for fold in folds:
        new_coordiantes = []
        if fold[0] == 'x':
            foldx = fold[1]
            for c in coordinates:
                if c[0] > foldx:
                    new_coord = (2*foldx - c[0]), c[1]
                else:
                    new_coord = (c[0], c[1])
                if new_coord not in new_coordiantes:
                        new_coordiantes.append(new_coord)
        if fold[0] == 'y':
            foldy = fold[1]
            for c in coordinates:
                if c[1] > foldy:
                    new_coord = (c[0], 2*foldy - c[1])
                else:
                    new_coord = (c[0], c[1])
                if new_coord not in new_coordiantes:
                        new_coordiantes.append(new_coord)
                    
        print("Fold " + fold[0] + " by " + str(fold[1]) + " New Coordinates = " 
            + str(len(new_coordiantes)))
        coordinates = new_coordiantes
    
    
    # PART 2
    system = [['.' for _ in range(max([c[0] for c in coordinates])+1)] 
        for _ in range(max([c[1] for c in coordinates])+1)]
    
    for c in coordinates:
        system[c[1]][c[0]] = '#'
        
    print("\n".join(["".join(s) for s in system]))