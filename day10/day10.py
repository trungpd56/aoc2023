#!/usr/bin/env python3

import sys
from collections import deque


tpipes = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def get_start_type(r, c):
    res = []
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        for drr, dcc in tpipes[lines[rr][cc]]:
            if drr + dr == 0 and dcc + dc == 0:
                res.append((dr, dc))
    assert len(res) == 2
    for k, vals in tpipes.items():
        if all(val in vals for val in res):
            return k
    return ""


def get_moves(r, c):
    return [(r + dr, c + dc) for dr, dc in tpipes[lines[r][c]]]


with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines()]

startr, startc = 0, 0
for startr, line in enumerate(lines):
    try:
        startc = line.index("S")
        break
    except:
        pass

lines[startr] = lines[startr].replace("S", get_start_type(startr, startc))

queue = deque([(startr, startc)])
seen = set()
while queue:
    r, c = queue.popleft()
    if (r, c) in seen:
        continue
    seen.add((r, c))
    for move in get_moves(r, c):
        queue.append(move)

part1 = len(seen) // 2
print(f"Part 1: {part1}")


lines2 = ""
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        lines2 += "." if (r, c) not in seen else ch
    lines2 += "\n"

lines2 = lines2.splitlines()
part2 = 0
for line in lines2:
    outside = True
    startF = None
    for ch in line:
        match ch:
            case ".":
                if not outside:
                    part2 += 1
            case "|":
                outside = not outside
            case "-":
                assert startF is not None
                pass
            case "F":
                startF = True
            case "L":
                startF = False
            case "J":
                if startF:
                    outside = not outside
                startF = None
            case "7":
                if not startF:
                    outside = not outside
                startF = None

print(f"Part 2: {part2}")
