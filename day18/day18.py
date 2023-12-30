#!/usr/bin/env python3

import sys


# https://en.wikipedia.org/wiki/Shoelace_formula
def calA(points: list) -> int:
    total = 0
    for p1, p2 in zip(points, points[1:] + [points[0]]):
        # breakpoint()
        total += (p1[1] + p2[1]) * (p1[0] - p2[0])
    return abs(total // 2)


def boundary(points: list) -> int:
    total = 0
    for p1, p2 in zip(points, points[1:] + [points[0]]):
        total += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return total


def get_points(lines: list[str], p2=False) -> list:
    r, c = 0, 0
    points = [(0, 0)]
    for line in lines:
        dir, val, hex = line.strip().split()
        val = int(val)
        if p2:
            hex = hex.strip("()#")
            dir = "RDLU"[int(hex[-1])]
            val = int(hex[:-1], 16)
        match dir:
            case "R":
                c += val
            case "L":
                c -= val
            case "U":
                r -= val
            case "D":
                r += val
        points.append((r, c))
    return points


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


# https://en.wikipedia.org/wiki/Pick%27s_theorem
# A = i + b/2 - 1
# i + b = A + b/2 + 1
points = get_points(lines)
part1 = calA(points) + boundary(points) / 2 + 1
print(f"Part 1: {part1}")

points2 = get_points(lines, True)
part2 = calA(points2) + boundary(points2) / 2 + 1
print(f"Part 2: {part2}")

