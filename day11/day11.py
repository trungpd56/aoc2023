#!/usr/bin/env python3

import sys
from itertools import combinations


def dist(p1, p2, diff=2):
    dist = 0
    for r in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
        dist += diff if r in empty_rows else 1
    for c in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
        dist += diff if c in empty_cols else 1
    return dist


with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines()]


galaxy = [
    (r, c) for r, row in enumerate(lines) for c, char in enumerate(row) if char == "#"
]
empty_rows = [r for r, line in enumerate(lines) if "#" not in line]
empty_cols = [c for c, col in enumerate(zip(*lines)) if "#" not in col]


part1 = sum(dist(p1, p2) for p1, p2 in combinations(galaxy, 2))
print(f"Part 1: {part1}")

part2 = sum(dist(p1, p2, 1000000) for p1, p2 in combinations(galaxy, 2))
print(f"Part 2: {part2}")
