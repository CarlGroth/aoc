with open('input/09.txt', 'r') as f:
    txt = f.read().splitlines()


def part1():
    head = 0j
    tail = 0j
    visited = set([head])
    lut = {
        'R': 1,
        'D': -1j,
        'L': -1,
        'U': 1j
    }
    moves = [(x.split()[0], int(x.split()[1])) for x in txt]
    for direction, length in moves:
        for _ in range(length):
            next_head = head + lut[direction]
            if (abs(next_head - tail) > 1.42):
                tail = head
            head = next_head
            visited.add(tail)
    print(len(visited))


def part2():
    head, *tail = [0j] * 10
    visited = set([head])
    lut = {
        'R': 1,
        'D': -1j,
        'L': -1,
        'U': 1j
    }
    moves = [(x.split()[0], int(x.split()[1])) for x in txt]
    for direction, length in moves:
        for _ in range(length):
            head += lut[direction]
            for i, segment in enumerate(tail):
                prev = tail[i-1] if i != 0 else head
                diff = prev - segment
                if abs(diff) > 1.42:
                    tail[i] += complex(min(max(diff.real, -1), 1),
                                       min(max(diff.imag, -1), 1))
            visited.add(tail[-1])

    print(len(visited))


part1()
part2()
