import json
from itertools import chain
from functools import cmp_to_key

with open('input/13.txt', 'r') as f:
    chunks = [tuple(map(json.loads, x.splitlines())) for x in f.read().split('\n\n')]

def compare(a, b):
    match a, b:
        case list(), list():
            for p in zip(a, b):
                if (res := compare(*p)):
                    return res
            return compare(len(a), len(b))
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])
        case int(), int():
            return (b < a) - (a < b)


def part1():
    print(sum(i for i, e in enumerate(chunks, start=1) if compare(*e) == -1))

def part2():
    chunks.extend([([[2]], [[6]])])
    flattened = sorted(chain.from_iterable(chunks), key=cmp_to_key(compare))
    two = flattened.index([[2]]) + 1
    six = flattened.index([[6]]) + 1
    print(two * six)

part1()
part2()