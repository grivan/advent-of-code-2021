INPUT = "day17/day17.in"


def within_target(x,y):
    if minT[0] <= x <= maxT[0] and minT[1] <= y <= maxT[1]:
        return True
    return False


def simulate(vx, vy):
    start_x, start_y = 0, 0
    max_y = start_y

    while start_x <= maxT[0] and start_y >= minT[1]:

        if within_target(start_x, start_y):
            return True, max_y

        start_x += vx
        start_y += vy

        if max_y < start_y:
            max_y = start_y

        if vx != 0:
            vx -= 1 if vx > 0 else -1
        vy -= 1

    return False, None


with open(INPUT) as infile:
    X,Y = infile.readline().rstrip()[13:].split(',')
    X = X[2:].split('..')
    Y = Y[3:].split('..')
    minT = (int(X[0]), int(Y[0]))
    maxT = (int(X[1]), int(Y[1]))

    maxYGlobal = None
    maxYVelocity = None
    total_count = 0
    for vx in range(0, maxT[0] + 1):
        for vy in range(-500, 500):  # could have done a better job with this guess!
            valid, maxY = simulate(vx, vy)
            if valid:
                total_count += 1
                if maxYGlobal and maxYGlobal > maxY:
                    maxYVelocity = vx, vy
                else:
                    maxYVelocity = vx, vy
                    maxYGlobal = maxY

    print("PART 1: " + str(maxYGlobal), "PART 2: " + str(total_count))