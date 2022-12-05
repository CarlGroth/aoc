import re

with open('input/05.txt', 'r') as f:
    start, moves = f.read().split('\n\n')
    moves = moves.split('\n')

regex = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_start():
    *moves, legend = start.split('\n')
    width = len(legend)
    out = [[] for _ in range(width // 4 + 1)]
    for move in reversed(moves):
        for i in range(1, width, 4):
            if move[i] != ' ':
                out[i // 4].append(move[i])

    return out


def parse_moves():
    return [tuple(int(g) for g in regex.findall(x)[0]) for x in moves]


def part1():
    s = parse_start()
    m = parse_moves()
    for amt, src, dst in m:
        for _ in range(amt):
            s[dst-1].append(s[src-1].pop())
    print(''.join(x[-1] for x in s))


def part2():
    s = parse_start()
    m = parse_moves()
    for amt, src, dst in m:
        boxes = reversed([s[src-1].pop() for _ in range(amt)])
        s[dst-1].extend(boxes)
    print(''.join(x[-1] for x in s))


part1()
part2()
