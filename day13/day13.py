#!/usr/bin/env python3

import sys


def pat(lines: list[str], diff: int = 0) -> int:
    for i in range(1, len(lines)):
        above = lines[:i][::-1]
        below = lines[i:]
        if (
            sum(sum(ac != bc for ac, bc in zip(ar, br)) for ar, br in zip(above, below))
            == diff
        ):
            return i
    return 0


with open(sys.argv[1], "r") as f:
    blocks = f.read().strip().split("\n\n")


def solve(blocks: list[str], diff: int = 0) -> int:
    cnt = 0
    for block in blocks:
        lines = block.splitlines()
        cnt += 100 * pat(lines, diff)
        cnt += pat(list(zip(*lines)), diff)
    return cnt


part1 = solve(blocks)
print(f"Part 1: {part1}")

part2 = solve(blocks, 1)
print(f"Part 2: {part2}")
