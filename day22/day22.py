#!/usr/bin/env python3

import sys
from collections import deque


class Brick:
    def __init__(self, line):
        points = [list(map(int, p.split(","))) for p in line.strip().split("~")]
        p1, p2 = sorted(points, key=lambda x: x[2])
        self.x1, self.y1, self.z1 = p1
        self.x2, self.y2, self.z2 = p2
        assert self.z2 >= self.z1
        self.supports = set()
        self.supported_by = set()

    def __repr__(self) -> str:
        return f"<Bricks {(self.x1, self.y1, self.z1)} {(self.x2, self.y2, self.z2)}>"

    def overlaps(self, other) -> bool:
        return max(self.x1, other.x1) <= min(self.x2, other.x2) and max(
            self.y1, other.y1
        ) <= min(self.y2, other.y2)


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

bricks = sorted([Brick(line) for line in lines], key=lambda x: x.z1)
for i, brick in enumerate(bricks):
    floor = 1
    for other in bricks[:i]:
        if brick.overlaps(other):
            floor = max(floor, other.z2 + 1)
    fall_distance = brick.z1 - floor
    brick.z1 -= fall_distance
    brick.z2 -= fall_distance

bricks.sort(key=lambda b: b.z1)

for i, brick in enumerate(bricks):
    for other in bricks[:i]:
        if brick.overlaps(other) and other.z2 == brick.z1 - 1:
            brick.supported_by.add(other)
            other.supports.add(brick)

part1 = 0
for brick in bricks:
    if all(len(other.supported_by) > 1 for other in brick.supports):
        part1 += 1

print(f"Part 1: {part1}")

part2 = 0
for brick in bricks:
    queue = deque([brick])
    falling = set()
    while queue:
        b = queue.popleft()
        if b in falling:
            continue
        falling.add(b)
        for other in b.supports:
            if other.supported_by <= falling:
                queue.append(other)
    part2 += len(falling) - 1

print(f"Part 2: {part2}")

