import itertools
import re
from dataclasses import dataclass
from typing import List

# bruh
regex = re.compile(
    r'Valve (\w+?) has flow rate=(\d+?); tunnels? leads? to valves? (.+)')


@dataclass
class Valve:
    id: str
    flow: int
    targets: List[str]


with open('input/16.txt', 'r') as f:
    lines = f.read().splitlines()


valves = [Valve(id=id, flow=int(flow), targets=targets.split(', '))
          for id, flow, targets in map(lambda x: regex.match(x).groups(), lines)]
valves.sort(key=lambda v: v.flow, reverse=True)
reverse_lookup = {e.id: i for i, e in enumerate(valves)}

start = reverse_lookup['AA']
n_positive = sum(x.flow > 0 for x in valves)
n = len(valves)
adj = [[] for _ in range(n)]
flow = [0] * n

for v in valves:
    idx = reverse_lookup[v.id]
    flow[idx] = v.flow
    for w in v.targets:
        adj[idx].append(reverse_lookup[w])


n_possible = 1 << n_positive
dp = [[[0]*n_possible for _ in range(n)] for _ in range(30)]
for time, idx in itertools.product(range(1, 30), range(n)):
    mask = 1 << idx
    for x in range(n_possible):
        best = dp[time][idx][x]
        if mask & x and time >= 1:
            best = max(dp[time-1][idx][x - mask] + flow[idx] * time, best)
        dp[time][idx][x] = max(max(dp[time-1][j][x] for j in adj[idx]), best)

print('Part 1:', dp[-1][start][-1])

highest = max(dp[25][start][x] + dp[25][start][y]
              for x in range(n_possible) for y in range(x) if x & y == 0)

print('Part 2:', highest)
