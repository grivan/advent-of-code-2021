
def extend(image):
    h = len(image)
    w = len(image[0])
    offset = 50
    new_image = [['.' for _ in range(w+offset*2)] for _ in range(h+offset*2)]

    for i in range(len(image)):
        for j in range(len(image[0])):
            new_image[i+offset][j+offset] = image[i][j]

    return new_image


def print_image(image):
    return "\n".join(["".join(x) for x in image])


def transform(eng, image):
    nine = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    new_image = [['.' for _ in range(len(image[0]))] for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            bin = []
            for x in nine:
                try:
                    bin.append(image[i+x[0]][j+x[1]])
                except IndexError:
                    bin.append(image[0][0])
            bin = ["0" if x == '.' else "1" for x in bin]
            index = int("".join(bin), 2)
            new_image[i][j] = eng[index]
    return new_image


with open("day20/day20.in") as infile:
    enh = infile.readline().rstrip()

    # read empty line
    infile.readline()

    imagelines = infile.readlines()
    image = []
    for line in imagelines:
        image.append(list(line.rstrip()))

    image = extend(image)
    # print(print_image(image))

    for k in range(50):
        image = transform(enh, image)

    lit = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '#':
                lit+=1

    print(lit)