INPUT = "day1.in"

def find_larger(input_file, window):
    
    previous = [None for _w in range(window)]
    larger = 0
    
    with open(input_file) as day1in:
        for depth in day1in:
            depth = int(depth)
            
            # handle edge conditions
            if not all(previous):
                previous.pop(0)
                previous.append(depth)
                continue
            
            # do the window comparison
            prev_sum = sum(previous)
            previous.pop(0)
            previous.append(depth)
            curr_sum = sum(previous)
            
            if curr_sum > prev_sum:
                larger+=1
    
    return larger
    
print(find_larger(INPUT, 3))