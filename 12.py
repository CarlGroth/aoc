from collections import deque

with open('input/12.txt', 'r') as f:
    chunks = f.read().splitlines()

HEIGHT = len(chunks)
WIDTH = len(chunks[0])

def get_height(pos):
    x, y = pos
    char = chunks[y][x]
    return ord({
        'S': 'a',
        'E': 'z'
    }.get(char, char)) - 97

def grid_contains(pos):
    x, y = pos
    return 0 <= x < WIDTH and 0 <= y < HEIGHT

def solve(starts, end):
    queue = deque()
    visited = set()
    distances = { start: 0 for start in starts }
    queue.extend(starts)
    while queue:
        u = queue.popleft()
        if u == end:
            continue
        x, y = u
        targets = (
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        )
        for v in targets:
            if v in visited:
                continue
            if not grid_contains(v):
                continue
            if get_height(v) - get_height(u) > 1:
                continue
            dist = distances[u] + 1
            if v not in distances or dist < distances[v]:
                distances[v] = dist
                visited.add(v)
                queue.append(v)

    print(distances[end])


def part1():
    starts = [(j, i) for i, row in enumerate(chunks) for j, e in enumerate(row) if e == 'S'][0]
    end = [(j, i) for i, row in enumerate(chunks) for j, e in enumerate(row) if e == 'E'][0]
    solve([starts], end)

def part2():
    starts = [(j, i) for i, row in enumerate(chunks) for j, e in enumerate(row) if e in 'aS']
    end = [(j, i) for i, row in enumerate(chunks) for j, e in enumerate(row) if e == 'E'][0]
    solve(starts, end)

part1()
part2()