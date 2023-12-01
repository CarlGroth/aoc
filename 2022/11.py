from functools import reduce
import operator
from dataclasses import dataclass
from typing import List, Optional, Tuple
import heapq

@dataclass
class Monkey:
    items: List[int]
    operation: Tuple[str, Optional[int], Optional[int]]
    test: int
    actions: Tuple[int, int]
    inspections: int = 0


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
        out.append(Monkey(items=items,operation=tuple(operation), test=test, actions=actions))
    return out

def part1():
    monkeys = parse()
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                new_val = apply(*monkey.operation, item) // 3
                target = monkey.actions[new_val % monkey.test == 0]
                monkeys[target].items.append(new_val)
            monkey.inspections += len(monkey.items)
            monkey.items.clear()
            
    a, b = heapq.nlargest(2, [m.inspections for m in monkeys])
    print(a * b)

def part2():
    monkeys = parse()
    scale = reduce(operator.mul, [monkey.test for monkey in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                new_val = apply(*monkey.operation, item) % scale
                target = monkey.actions[new_val % monkey.test == 0]
                monkeys[target].items.append(new_val)
            monkey.inspections += len(monkey.items)
            monkey.items.clear()

    a, b = heapq.nlargest(2, [m.inspections for m in monkeys])
    print(a * b)

part1()
part2()