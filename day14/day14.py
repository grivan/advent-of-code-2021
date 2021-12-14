from collections import Counter, defaultdict
import math

INPUT = "day14/day14.in"

with open(INPUT) as infile:
    template = infile.readline().rstrip()
    tparis = defaultdict(int)
    for i in range(len(template) -1):
        tparis[template[i]+template[i+1]]+=1
    
    # discard empty
    infile.readline()
    
    trans = {}
    for line in infile:
        start, end = line.rstrip().split(' -> ')
        trans[start] = [start[0]+end, end+start[1]]
       
    iterations = 40
    for i in range(iterations):
        start = defaultdict(int)
        for elem in tparis:
            if elem in trans:
                for t in trans[elem]:
                    start[t]+=tparis[elem]
        tparis = start
    
    chars = defaultdict(int)
    for pair in tparis:
        chars[pair[0]]+=tparis[pair]
        chars[pair[1]]+=tparis[pair]
    
    most_common = max(dict(chars), key=lambda key: chars[key])
    least_common = min(dict(chars), key=lambda key: chars[key])
    
    print(math.ceil(chars[most_common]/2)-math.ceil(chars[least_common]/2))