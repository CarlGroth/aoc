from functools import reduce
import operator
import math

with open('input/11.txt', 'r') as f:
    chunks = f.read().split('\n\n')

def apply(op, a, b, old):
    lut = {
        '+': operator.add,
        '*': operator.mul,
    }
    return lut[op](a or old, b or old)

def parse():
    out = []
    for chunk in chunks:
        _, starting, operation, test, true_test, false_test = chunk.splitlines()
        items = list(map(int, starting.split(':')[1].split(', ')))
        left, op, right = operation.split('=')[-1].split()
        operation = [op] + [int(x) if x.isnumeric() else None for x in [left, right]]
        test = int(test.split()[-1])
        actions = (int(false_test.split()[-1]), int(true_test.split()[-1]))
        out.append([items, operation, test, actions])
    return out

def part1():
    monkeys = parse()
    inspections = [0]*len(monkeys)
    for _ in range(20):
        for i, (items, operation, test, actions) in enumerate(monkeys):
            inspections[i] += len(items)
            for item in items:
                new_val = apply(*operation, item) // 3
                target = actions[new_val % test == 0]
                monkeys[target][0].append(new_val)
            monkeys[i][0].clear()
    a, b, *_ = sorted(inspections, reverse=True)
    print(a * b)

def part2():
    monkeys = parse()
    inspections = [0]*len(monkeys)
    scale = reduce(operator.mul, [x[2] for x in monkeys])
    for _ in range(10000):
        for i, (items, operation, test, actions) in enumerate(monkeys):
            inspections[i] += len(items)
            for item in items:
                new_val = apply(*operation, item) % scale
                target = actions[new_val % test == 0]
                monkeys[target][0].append(new_val)
            monkeys[i][0].clear()

    a, b, *_ = sorted(inspections, reverse=True)
    print(a * b)

part1()
part2()