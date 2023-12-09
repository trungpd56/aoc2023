#!/usr/bin/env python3

import sys
import re
from itertools import cycle
import math


with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    dir = dict(R=1, L=0)
    nodes = {}
    init = [dir[c] for c in lines[0].strip()]
    for line in lines[2:]:
        src, left, right = re.findall(r"[A-Z0-9]+", line)
        nodes[src] = [left, right]

cnt = 0
node = "AAA"
for d in cycle(init):
    node = nodes[node][d]
    cnt += 1
    if node == "ZZZ":
        break

part1 = cnt
print(f"Part 1: {part1}")

snodes = [n for n in nodes if n[-1] == "A"]
enodes = [n for n in nodes if n[-1] == "Z"]
res = [0] * len(snodes)
cnt = 0
for d in cycle(init):
    cnt += 1
    for i, n in enumerate(snodes.copy()):
        if (nnode := nodes[n][d]) in enodes:
            res[i] = cnt
        snodes[i] = nnode
    if all(r != 0 for r in res):
        break

part2 = math.lcm(*res)
print(f"Part 2: {part2}")
