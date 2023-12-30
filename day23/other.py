#!/usr/bin/env python3
import sys
from collections import deque


def solve(part2=False):
    jmap = {}
    for jr, jc in junctions:
        jmap[(jr, jc)] = {}

        queue = deque([(jr, jc, 0)])
        seen = set()
        while queue:
            r, c, s = queue.popleft()
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if (r, c) != (jr, jc) and (r, c) in junctions:
                jmap[(jr, jc)][(r, c)] = s
                continue

            match grid[r][c]:
                case "^":
                    next_steps = [(-1, 0)]
                case "v":
                    next_steps = [(1, 0)]
                case ">":
                    next_steps = [(0, 1)]
                case "<":
                    next_steps = [(0, -1)]
                case ".":
                    next_steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                case _:
                    assert False
            if part2:
                next_steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in next_steps:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] != "#":
                    queue.append((nr, nc, s + 1))

    queue = deque([(*start, [(*start,)])])
    paths = []
    while queue:
        r, c, path = queue.pop()

        if (r, c) == end:
            paths.append(path)
            continue

        for next_point, d in jmap[(r, c)].items():
            if next_point not in path:
                queue.append((*next_point, path + [next_point]))

    longest = 0
    for path in paths:
        longest = max(longest, sum(jmap[p1][p2] for p1, p2 in zip(path, path[1:])))
    return longest


with open(sys.argv[1], "r") as f:
    grid = [l.strip() for l in f.readlines()]

height = len(grid)
width = len(grid[0])
start = (0, grid[0].index("."))
end = (len(grid) - 1, grid[-1].index("."))

junctions = [start, end]
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        num_neighbors = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] != "#":
                num_neighbors += 1
        if num_neighbors > 2:
            junctions.append((r, c))


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(part2=True)}")

