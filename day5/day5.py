INPUT = "day5/day5.in"

# 1. generate the entire set of points covered by each line
# 2. find the common points between each two lines within a set

intersect = set()

lines = [] # [[(x1,y1),(x2,y2)]]


def generate_points(line):
    
    x1, y1 = line[0][0], line[0][1]
    x2, y2 = line[1][0], line[1][1]
    
    if x1 == x2 and y1 == y2:
        return set((x1,x1))
    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        return set([(x1, y) for y in range(y1, y2+1)])
    elif y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        return set([(x, y1) for x in range(x1, x2+1)])
    else:
        dx = x2 - x1
        dy = y2 - y1
        slope = dx/dy
        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        points = []
        y = y1
        for x in range(x1, x2+1):
            points.append((x, y))
            y += slope
        return set(points)

def print_mat(lines_points):
    all_points = set()
    for line_point in lines_points:
        for point in line_point:
            all_points.add(point)
    
    mat = [[0 for i in range(10)] for i in range(10)]
    for i in range(10):
        for j in range(10):
            if (i,j) in all_points:
                mat[i][j]=1
        
    for i in range(10):
        for j in range(10):
            if (i, j) in intersect:
                mat[i][j]+=1
    
    for row in mat:
        print(row)

with open(INPUT) as infile:
    for line in infile:
        linestr = line.rstrip().split('->');
        x1, y1 = map(int, linestr[0].split(','))
        x2, y2 = map(int, linestr[1].split(','))
        lines.append(((x1, y1), (x2, y2)))
    
    lines_points = [generate_points(line) for line in lines]
    
    intersect = set()
    for line_points in lines_points:
        if len(line_points) > 0:
            for line_points2 in lines_points:
                if len(line_points2) > 0 and line_points != line_points2:
                    intersect.update(line_points.intersection(line_points2))
    
    # print_mat(lines_points)
    print(len(intersect))