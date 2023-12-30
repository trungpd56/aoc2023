#!/usr/bin/env python3

import heapq
import sys

with open(sys.argv[1], "r") as f:
    lines = [[int(c) for c in line.strip()] for line in f.readlines()]

maxr = len(lines)
maxc = len(lines[0])


def cnt(maxd: int = 3, p2=False):
    seen = set()
    queue = [(0, 0, 0, 0, 0, 0)]
    while queue:
        heat, r, c, dr, dc, s = heapq.heappop(queue)
        if (r, c, dr, dc, s) in seen:
            continue
        seen.add((r, c, dr, dc, s))
        if (r, c) == (maxr - 1, maxc - 1):
            if not p2:
                return heat
            if s >= 4:
                return heat
        for drr, dcc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + drr
            cc = c + dcc
            if not (0 <= rr < maxr and 0 <= cc < maxc):
                continue
            if drr == -dr and dcc == -dc:
                continue
            if drr == dr and dcc == dc:
                if s < maxd:
                    heapq.heappush(
                        queue, (heat + lines[rr][cc], rr, cc, drr, dcc, s + 1)
                    )
                else:
                    continue
            else:
                if not p2:
                    heapq.heappush(queue, (heat + lines[rr][cc], rr, cc, drr, dcc, 1))
                elif s >= 4 or (dr == 0 and dc == 0):
                    heapq.heappush(queue, (heat + lines[rr][cc], rr, cc, drr, dcc, 1))


part1 = cnt()
print(f"Part 1: {part1}")

part2 = cnt(10, True)
print(f"Part 2: {part2}")
