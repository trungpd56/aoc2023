#!/usr/bin/env python3

import sys
from collections import deque

with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines()]

maxr = len(lines)
maxc = len(lines[0])


def cnt(sr, sc, sdr, sdc):
    seen = set()
    queue = deque([(sr, sc, sdr, sdc)])
    while queue:
        r, c, dr, dc = queue.popleft()
        if (r, c, dr, dc) in seen:
            continue
        seen.add((r, c, dr, dc))
        nmoves = []
        match lines[r][c]:
            case ".":
                nmoves.append((dr, dc))
            case "\\":
                nmoves.append((dc, dr))
            case "/":
                nmoves.append((-dc, -dr))
            case "-":
                if dr == 0:
                    nmoves.append((dr, dc))
                else:
                    nmoves.extend([(0, dr), (0, -dr)])
            case "|":
                if dc == 0:
                    nmoves.append((dr, dc))
                else:
                    nmoves.extend([(-dc, 0), (dc, 0)])
        for drr, dcc in nmoves:
            rr, cc = r + drr, c + dcc
            if 0 <= rr < maxr and 0 <= cc < maxc:
                queue.append((rr, cc, drr, dcc))
    return len(set((r, c) for r, c, *_ in seen))


part1 = cnt(0, 0, 0, 1)
print(f"Part 1: {part1}")

part2 = 0
for r in range(maxr):
    part2 = max(cnt(r, 0, 0, 1), part2)
    part2 = max(cnt(r, maxc - 1, 0, -1), part2)
for c in range(maxc):
    part2 = max(cnt(0, c, 1, 0), part2)
    part2 = max(cnt(maxr - 1, c, -1, 0), part2)

print(f"Part 2: {part2}")

