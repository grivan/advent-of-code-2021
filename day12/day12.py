from collections import defaultdict
from copy import copy

INPUT = "day12/day12.in"

def find_path(current_path, paths, single):
    
    current = current_path[-1]
    if current == 'end':
        all_paths.add(",".join(current_path))
        return
    
    for path in paths[current]:
        
        if path == 'start':
            continue
        
        if path.islower():
            if path != single:
                if path in current_path:
                    continue
            else:
                if current_path.count(path) == 2:
                    continue
        
        current_path.append(path)
        find_path(current_path, paths, single)
        del current_path[-1]
    
    
with open(INPUT) as infile:
    paths = defaultdict(set)
    small = set()
    all_paths = set()
    
    for line in infile:
        e1, e2 = line.rstrip().split('-')
        paths[e1].add(e2)
        paths[e2].add(e1)
    
    for path in paths:
        if path.islower() and path not in ['start', 'end']:
            small.add(path)
    
    for s in small:
        find_path(['start'], paths, None)
    print("PART 1: " + str(len(all_paths)))
    
    all_paths = set()
    for s in small:
        find_path(['start'], paths, s)
        
    print("PART 2: " + str(len(all_paths)))