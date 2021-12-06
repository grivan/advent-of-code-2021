from collections import defaultdict

INPUT = "day6/day6.in"
DAY = 256

with open(INPUT) as infile:
    start = infile.readline().rstrip().split(',')
    start_fish = [int(fish) for fish in start]
    
    fish_map = defaultdict(int)
    for fish in start_fish:
        fish_map[fish]+= 1

    while(DAY > 0):
        new_fish_map = defaultdict(int)
        DAY-=1
        
        for spawn in fish_map.keys():
            
            if spawn == 0:
                new_fish_map[8] += fish_map[spawn]
                new_fish_map[6] += fish_map[spawn]
            else:
                new_fish_map[spawn-1] += fish_map[spawn]
        
        fish_map = new_fish_map
    
    print(sum(fish_map.values()))