import math


class Pair:

    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

    @staticmethod
    def from_str(treestr):
        return Pair.from_list(eval(treestr))

    @staticmethod
    def from_list(treelist, root=None):
        pair = Pair(root, None, None)
        if type(treelist[0]) == list:
            pair.left = Pair.from_list(treelist[0], pair)
        else:
            pair.left = treelist[0]
        if type(treelist[1]) == list:
            pair.right = Pair.from_list(treelist[1], pair)
        else:
            pair.right = treelist[1]
        return pair

    def add(self, pair):
        npair = Pair(None, self, pair)
        self.parent = npair
        pair.parent = npair
        return npair.reduce()

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"

    def split(self):
        # return true if a split happens
        pair = self._split_pair()

        if not pair:
            return False
        if not isinstance(pair.left, Pair) and pair.left > 9:
            pair.left = Pair(pair, math.floor(pair.left / 2), math.ceil(pair.left / 2))
        else:
            pair.right = Pair(pair, math.floor(pair.right / 2), math.ceil(pair.right / 2))

        return True

    def explode(self):
        pair = self._explode_pair(4)

        if not pair:
            return False

        parent = pair.parent
        if parent.left == pair:
            # set the left to 0
            parent.left = 0

            current = parent.parent
            while current and current.left == parent:
                parent = current
                current = parent.parent
            if current:
                if isinstance(current.left, Pair):
                    current = current.left
                    while isinstance(current.right, Pair):
                        current = current.right
                    current.right += pair.left
                else:
                    current.left += pair.left

            parent = pair.parent
            if isinstance(parent.right, Pair):
                current = parent.right
                while isinstance(current.left, Pair):
                    current = current.left
                current.left += pair.right
            else:
                parent.right += pair.right

        elif parent.right == pair:
            parent.right = 0

            if isinstance(parent.left, Pair):
                current = parent.left
                while isinstance(current.right, Pair):
                    current = current.right
                current.right += pair.left
            else:
                parent.left += pair.left

            current = parent.parent
            while current and current.right == parent:
                parent = current
                current = parent.parent
            if current:
                if isinstance(current.right, Pair):
                    current = current.right
                    while isinstance(current.left, Pair):
                        current = current.left
                    current.left += pair.right
                else:
                    current.right += pair.right

        return True

    def _split_pair(self):
        if isinstance(self.left, Pair):
            split_left = self.left._split_pair()
            if split_left:
                return split_left
        elif self.left > 9:
            return self
        if isinstance(self.right, Pair):
            split_right = self.right._split_pair()
            if split_right:
                return split_right
        elif self.right > 9:
            return self

    def _explode_pair(self, height):
        if height == 0:
            return self
        if isinstance(self.left, Pair):
            left_explode = self.left._explode_pair(height-1)
            if left_explode:
                return left_explode
        if isinstance(self.right, Pair):
            right_explode = self.right._explode_pair(height-1)
            if right_explode:
                return right_explode
        return None

    def reduce(self):
        action = True
        while action:
            if self.explode():
                continue
            if self.split():
                continue
            action = False
        return self

    def magnitue(self):
        total = 0
        if isinstance(self.right, Pair):
            total += 2 * self.right.magnitue()
        else:
            total += 2 * self.right
        if isinstance(self.left, Pair):
            total += 3 * self.left.magnitue()
        else:
            total += 3 * self.left
        return total


# magnitude tests
print("Starting Magnitude Tests..")
assert Pair.from_str("[1,9]").magnitue() == 21
assert Pair.from_str("[9,1]").magnitue() == 29
assert Pair.from_str("[[1,2],[[3,4],5]]").magnitue() == 143
assert Pair.from_str("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").magnitue() == 1384
assert Pair.from_str("[[[[1,1],[2,2]],[3,3]],[4,4]]").magnitue() == 445
assert Pair.from_str("[[[[3,0],[5,3]],[4,4]],[5,5]]").magnitue() == 791
assert Pair.from_str("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").magnitue() == 3488
print("Passed Magnitude Tests!")

# explode Tests
print("Starting Explode Tests..")

pair = Pair.from_str("[[[[[9,8],1],2],3],4]")
pair.explode()
assert str(pair) == "[[[[0,9],2],3],4]", str(pair)

pair = Pair.from_str("[7,[6,[5,[4,[3,2]]]]]")
pair.explode()
assert str(pair) == "[7,[6,[5,[7,0]]]]", str(pair)

pair = Pair.from_str("[[6,[5,[4,[3,2]]]],1]")
pair.explode()
assert str(pair) == "[[6,[5,[7,0]]],3]", str(pair)

pair = Pair.from_str("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
pair.explode()
assert str(pair) == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", str(pair)
pair.explode()
assert str(pair) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]", str(pair)

pair = Pair.from_str("[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]")
pair.explode()
assert str(pair) == "[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]", str(pair)

pair = Pair.from_str("[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]")
pair.explode()
assert str(pair) == "[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]", str(pair)

print("Explode Tests Pass!")

# split tests
print("Starting Split Tests..")

pair = Pair.from_str("[[[[0,7],4],[15,[0,13]]],[1,1]]")
pair.split()
assert str(pair) == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]", str(pair)

pair = Pair.from_str("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
pair.split()
assert str(pair) == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]", str(pair)

print("Split Tests Pass!")

# sum tests
print("Starting Sum Tests...")

print("Start Sum 1")
pair = Pair.from_str("[1,1]")
pair = pair.add(Pair.from_str("[2,2]"))
pair = pair.add(Pair.from_str("[3,3]"))
pair = pair.add(Pair.from_str("[4,4]"))
assert str(pair) == "[[[[1,1],[2,2]],[3,3]],[4,4]]", str(pair)

print("Start Sum 2")
pair = Pair.from_str("[1,1]")
pair = pair.add(Pair.from_str("[2,2]"))
pair = pair.add(Pair.from_str("[3,3]"))
pair = pair.add(Pair.from_str("[4,4]"))
pair = pair.add(Pair.from_str("[5,5]"))
assert str(pair) == "[[[[3,0],[5,3]],[4,4]],[5,5]]", str(pair)

print("Start Sum 3")
pair = Pair.from_str("[1,1]")
pair = pair.add(Pair.from_str("[2,2]"))
pair = pair.add(Pair.from_str("[3,3]"))
pair = pair.add(Pair.from_str("[4,4]"))
pair = pair.add(Pair.from_str("[5,5]"))
pair = pair.add(Pair.from_str("[6,6]"))
assert str(pair) == "[[[[5,0],[7,4]],[5,5]],[6,6]]", str(pair)

print("Start Sum 4")
pair = Pair.from_str("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
pair = pair.add(Pair.from_str("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"))
assert str(pair) == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]", str(pair)
pair = pair.add(Pair.from_str("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]"))
assert str(pair) == "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]", str(pair)
pair = pair.add(Pair.from_str("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"))
pair = pair.add(Pair.from_str("[7,[5,[[3,8],[1,4]]]]"))
pair = pair.add(Pair.from_str("[[2,[2,2]],[8,[8,1]]]"))
pair = pair.add(Pair.from_str("[2,9]"))
pair = pair.add(Pair.from_str("[1,[[[9,3],9],[[9,0],[0,7]]]]"))
pair = pair.add(Pair.from_str("[[[5,[7,4]],7],1]"))
pair = pair.add(Pair.from_str("[[[[4,2],2],6],[8,7]]"))
assert str(pair) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", str(pair)

print("Start Sum 5")
pair = Pair.from_str("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]")
pair = pair.add(Pair.from_str("[[[5,[2,8]],4],[5,[[9,9],0]]]"))
pair = pair.add(Pair.from_str("[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]"))
pair = pair.add(Pair.from_str("[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]"))
pair = pair.add(Pair.from_str("[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]"))
pair = pair.add(Pair.from_str("[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]"))
pair = pair.add(Pair.from_str("[[[[5,4],[7,7]],8],[[8,3],8]]"))
pair = pair.add(Pair.from_str("[[9,3],[[9,9],[6,[4,9]]]]"))
pair = pair.add(Pair.from_str("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]"))
pair = pair.add(Pair.from_str("[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"))
assert str(pair) == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", str(pair)

print("Sum Tests Pass")

with open("day18/day18.in") as infile:
    pair = None
    lines = infile.readlines()

    for line in lines:
        if pair:
            pair = pair.add(Pair.from_str(line.rstrip()))
        else:
            pair = Pair.from_str(line.rstrip())

    print("PART 1: ", pair.magnitue())

    max_mag = 0

    for line1 in lines:
        for line2 in lines:
            if line1 == line2:
                continue
            mag = Pair.from_str(line1.rstrip()).add(Pair.from_str(line2.rstrip())).magnitue()
            if mag > max_mag:
                max_mag = mag

    print("PART 2: ", max_mag)
