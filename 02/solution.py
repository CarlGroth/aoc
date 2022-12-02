with open('input.txt', 'r') as f:
    arr = f.read().split('\n')


def part1():
    moves = [(ord(a.split()[0]) - 64, ord(a.split()[1]) - 87) for a in arr]
    score = sum(us + 6 * (us - them % 3 == 1) + 3 * (us == them)
                for them, us in moves)
    print(score)


def part2():
    moves = [(ord(a.split()[0]) - 65, ord(a.split()[1]) - 88) for a in arr]
    lookup = [
        [3, 4, 8],
        [1, 5, 9],
        [2, 6, 7]
    ]
    score = sum(lookup[them][us] for them, us in moves)
    print(score)


part1()
part2()
