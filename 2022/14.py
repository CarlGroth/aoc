with open('input/14.txt', 'r') as f:
    lines = f.read().splitlines()


def form_cave():
    cave = set()
    for line in lines:
        segments = line.split(' -> ')
        for start, end in zip(segments, segments[1:]):
            # There has to be a better way to do this
            sx, sy = map(int, start.split(','))
            ex, ey = map(int, end.split(','))
            x, xx = sorted([sx, ex])
            y, yy = sorted([sy, ey])

            for x in range(x, xx+1):
                for y in range(y, yy+1):
                    cave.add(complex(x, y))
    highest = max(x.imag for x in cave)
    return cave, highest


def visit(pos):
    for diff in (1j, -1+1j, 1+1j):
        yield pos + diff


def part1():
    cave, highest = form_cave()
    grains = 0
    while True:
        pos = 500+0j
        while True:
            if pos.imag > highest:
                return grains

            for potential in visit(pos):
                if potential not in cave:
                    pos = potential
                    break
            else:
                grains += 1
                cave.add(pos)
                break


def part2():
    cave, highest = form_cave()
    floor = highest + 1
    grains = 0
    while True:
        pos = 500+0j
        if pos in cave:
            return grains
        while True:
            if pos.imag == floor:
                break

            for potential in visit(pos):
                if potential not in cave:
                    pos = potential
                    break
            else:
                break

        grains += 1
        cave.add(pos)


print(part1())
print(part2())
