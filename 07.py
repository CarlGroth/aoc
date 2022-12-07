from collections import defaultdict as dd
from json import dumps

with open('input/07.txt', 'r') as f:
    txt = f.read().splitlines()


def traverse(tree, name, sizes):
    out = 0
    for k, v in tree.items():
        if k == '..':
            continue
        if isinstance(v, int):
            out += v
        else:
            out += traverse(v, f'{name}/{k}', sizes)
    sizes[name] = out
    return out


def parse():
    tree = {}
    current = tree
    commands = [x.split() for x in txt]
    for a, b, *c in commands:
        if b == 'cd':
            target = c[0]
            if target == '/':
                current = tree
            elif target == '..':
                current = current['..']
            else:
                current.setdefault(target, {'..': current})
                current = current[target]
        elif a.isnumeric():
            filename = b
            current[filename] = int(a)
    return tree


def part1():
    tree = parse()
    sizes = {}
    traverse(tree, '', sizes)
    print(sum(v for v in sizes.values() if v < 100000))


def part2():
    tree = parse()
    sizes = {}
    traverse(tree, '', sizes)
    total = 70000000
    target = 30000000
    curr = sizes['']
    smallest_delete = curr - (total - target)
    print(min(x for x in sizes.values() if x > smallest_delete))


part1()
part2()
