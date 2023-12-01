import itertools
import re

with open('input/15.txt', 'r') as f:
    lines = f.read().splitlines()


def parse():
    regex = re.compile(r'-?\d+')
    return [tuple(map(int, regex.findall(x))) for x in lines]


def part1():
    data = parse()
    level = 2000000
    maybe, nope = set(), set()
    for x, y, sx, sy in data:
        if sy == level:
            nope.add(sx)
        # Beautiful
        width = (2 * (abs(x - sx) + abs(y - sy)) + 1 - 2 * abs(y - level)) // 2
        maybe |= set(range(x - width, x + width + 1))
    print(len(maybe - nope))


def diamond(sx, sy, dx, dy, N):
    manhattan = abs(sx - dx) + abs(sy - dy)
    vertical = range(max(sy - manhattan, 0), min(sy + manhattan + 1, N))
    for y in vertical:
        width = (2 * manhattan - 2 * abs(sy - y)) // 2
        yield y, range(sx - width, sx + width + 1)


def merge(ranges):
    ranges = sorted(ranges, key=lambda r: r.start)
    merged, remaining = ranges[:1], ranges[1:]

    for r in remaining:
        prev = merged[-1]

        if r.start <= prev.stop:
            merged[-1] = range(min(prev.start, r.start),
                               max(prev.stop, r.stop))
        else:
            merged.append(r)

    return merged


def part2():
    data = parse()
    N = 4000000
    ranges = [[] for _ in range(N)]
    # Keep your enemies on their toes by using
    # incomprehensible variable names
    for x, y, sx, sy in data:
        for yy, x_range in diamond(x, y, sx, sy, N):
            ranges[yy].append(x_range)
    y, x = next((y, x[0].stop) for y, x in enumerate(
        map(merge, ranges)) if len(x) == 2)
    print(x * 4000000 + y)


part1()
part2()
