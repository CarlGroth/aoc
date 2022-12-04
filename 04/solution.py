
with open('input.txt', 'r') as f:
    arr = f.read().split('\n')


def part1():
    sections = [[tuple(map(int, y.split('-')))
                 for y in x.split(',')] for x in arr]
    print(sum(rl <= ll and rh >= lh or ll <= rl and lh >=
          rh for (ll, lh), (rl, rh) in sections))


def part2():
    sections = [[tuple(map(int, y.split('-')))
                 for y in x.split(',')] for x in arr]
    print(sum(ll <= rh and rl <= lh for (ll, lh), (rl, rh) in sections))


part1()
part2()
