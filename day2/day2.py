INPUT = "day2/day2.in"

def find_position(input_file):
    
    hpos = 0
    depth = 0
    aim = 0
    
    with open(input_file) as moves:
        for move_str in moves:
            move, amount = move_str.rstrip().split(' ')
            amount = int(amount)
            
            if move == 'forward':
                hpos+=amount
                depth+=aim*amount
                
            elif move == 'down':
                aim+=amount
            
            elif move == 'up':
                aim-=amount
            
    return hpos, depth

hpos, depth = find_position(INPUT)
print(hpos*depth)