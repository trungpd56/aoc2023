#!/usr/bin/env python3

import sys
from collections import deque

with open(sys.argv[1], "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

startr, startc = 0, 0
for startr, line in enumerate(lines):
    try:
        startc = line.index("S")
        break
    except:
        continue

maxr = len(lines)
maxc = len(lines[0])
lines[startr][startc] = "."


def cnt_step(n: int = 64):
    queue = deque([(startr, startc, 0)])
    seen = set()
    cnt = 0
    while queue:
        r, c, step = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if not step % 2:
            cnt += 1
        if step == n + 1:
            return cnt
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if lines[rr % maxr][cc % maxc] != "#":
                queue.append((rr, cc, step + 1))


part1 = cnt_step()
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")

