
class Cuboid:

    def __init__(self, cord, sign):
        self.x1 = cord[0][0]
        self.x2 = cord[0][1]
        self.y1 = cord[1][0]
        self.y2 = cord[1][1]
        self.z1 = cord[2][0]
        self.z2 = cord[2][1]
        self.sign = sign

    def intersect(self, c):
        if self.x2 >= c.x1 and self.x1 <= c.x2:
            if self.y2 >= c.y1 and self.y1 <= c.y2:
                if self.z2 >= c.z1 and self.z1 <= c.z2:
                    return Cuboid(
                        (
                            (max(self.x1, c.x1), min(self.x2, c.x2)),
                            (max(self.y1, c.y1), min(self.y2, c.y2)),
                            (max(self.z1, c.z1), min(self.z2, c.z2)),
                        ),
                        -c.sign
                    )

    def volume(self):
        return self.sign * abs((self.x2 - self.x1 + 1)) * abs((self.y2 - self.y1 + 1)) * abs((self.z2 - self.z1 + 1))

    def is_initial(self):
        return all(map(lambda x: abs(x) <= 50, [self.x1, self.x2, self.y1, self.y2, self.z1, self.z2]))

    def __str__(self):
        return "X=({}, {}), Y=({}, {}), Z=({}, {}), sign={}".format(self.x1, self.x2, self.y1, self.y2,
                                                                    self.z1, self.z2, self.sign)


with open("day22/day22.in") as infile:
    commands = []
    for line in infile:
        c, cord = line.rstrip().split(' ')
        cord = [y[1].split('..') for y in [x.split('=') for x in cord.split(',')]]
        cord = [(int(x[0]), int(x[1])) for x in cord]
        c = 1 if c == 'on' else -1
        commands.append((c, cord))

    cubiods = []
    for command, cord in commands:
        new_cubiod = Cuboid(cord, command)
        if not new_cubiod.is_initial():
            continue
        update = []
        for cube in cubiods:
            intersection = new_cubiod.intersect(cube)
            if intersection:
                update.append(intersection)
        if command > 0:
            update.append(new_cubiod)
        cubiods.extend(update)

    print("PART1: " + str(sum(map(lambda x: x.volume(), cubiods))))


    cubiods = []
    for command, cord in commands:
        new_cubiod = Cuboid(cord, command)
        update = []
        for cube in cubiods:
            intersection = new_cubiod.intersect(cube)
            if intersection:
                update.append(intersection)
        if command > 0:
            update.append(new_cubiod)
        cubiods.extend(update)

    print("PART2: " + str(sum(map(lambda x: x.volume(), cubiods))))
