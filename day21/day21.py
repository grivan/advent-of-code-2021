from collections import defaultdict

with open("day21/day21.in") as infile:
    p1o = infile.readline().rstrip().split(':')
    p2o = infile.readline().rstrip().split(':')

    p1 = int(p1o[1])
    p2 = int(p2o[1])

    p1score = 0
    p2score = 0

    losing_score = None
    plays = None

    play = 1

    for i in range(0, 1000, 3):

        i1 = i % 100 + 1
        i2 = (i + 1) % 100 + 1
        i3 = (i + 2) % 100 + 1

        total = i1 + i2 + i3

        if play:
            p1 = (p1 + total) % 10
            p1score += p1 if p1 else 10
            play = 0
        else:
            p2 = (p2 + total) % 10
            p2score += p2 if p2 else 10
            play = 1

        if p1score >= 1000 or p2score >= 1000:
            losing_score = p1score if p1score < p2score else p2score
            plays = i + 3
            break

    print("PART 1: " + str(plays * losing_score))

    die = [i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1,4)]
    game_state = {(int(p1o[1]), int(p2o[1]), 0, 0, True): 1}  # {[p1, p2, p1score, p2score, play]: 1, ...}
    p1total = 0
    p2total = 0

    i = 0
    while len(game_state) > 0:
        i += 1
        new_state = defaultdict(int)
        for state, snum in game_state.items():
            for total in die:
                p1, p2, p1score, p2score, play = state
                if play:
                    p1 = (p1 + total) % 10
                    p1score += p1 if p1 else 10
                else:
                    p2 = (p2 + total) % 10
                    p2score += p2 if p2 else 10
                if p1score >= 21:
                    p1total += snum
                elif p2score >= 21:
                    p2total += snum
                else:
                    new_state[(p1, p2, p1score, p2score, not play)] += snum

        game_state = new_state

    print("PART 2: " + str(max(p1total, p2total)))
