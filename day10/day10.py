INPUT = "day10/day10.in"

with open(INPUT) as infile:
    
    pts = {
        ')':3,
        ']':57,
        '}':1197,
        '>':25137,
    }
    
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    
    scores = {
        ')':1,
        ']':2,
        '}':3,
        '>':4,
    }
    
    illegal = []
    incomplete = []
    
    for line in infile:
        illegalline = False 
        stack = []
        for char in line.rstrip():
            if char in pairs:
                stack.append(pairs[char])
            else:
                schar = stack.pop()
                if schar != char:
                    illegal.append(char)
                    illegalline = True
            if illegalline:
                break
            
        if not illegalline:
            incomplete.append(reversed(stack))
    
    total = 0
    for char in illegal:
        total+=pts[char]
        
    print(total)
    
    totalpt2 = []
    for line in incomplete:
        ltotal = 0
        for char in line:
            ltotal=5*ltotal+scores[char]
        totalpt2.append(ltotal)
            
    print(sorted(totalpt2)[int(len(totalpt2)/2)])