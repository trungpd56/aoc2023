#!/usr/bin/env python3

import sys
from itertools import combinations


def expanse(image: list[str], n:int =1) -> list[str]:
    nlist = []
    for line in image:
        nlist.append(line)
        if all(c == "." for c in line):
            for _ in range(n):
                nlist.append(line)
    ncols = []
    for line in zip(*nlist):
        ncols.append(line)
        if all(c == "." for c in line):
            for _ in range(n):
                ncols.append(line)
    return list(zip(*ncols))


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open(sys.argv[1], "r") as f:
    image = [line.strip() for line in f.readlines()]

nimage = expanse(image)
points = []
for r, line in enumerate(nimage):
    for c, char in enumerate(line):
        if char == "#":
            points.append((r, c))

memo = {}
coms = combinations(points, 2)


part1 = sum(dist(*c) for c in coms)
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")
