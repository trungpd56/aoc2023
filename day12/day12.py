#!/usr/bin/env python3

import sys
from functools import cache


@cache
def solve(spring: str, nums: tuple) -> int:
    if len(spring) == 0:
        if len(nums) == 0:
            return 1
        return 0
    if len(nums) == 0:
        if "#" in spring:
            return 0
        return 1

    if len(spring) < sum(nums):
        return 0

    cnt = 0
    ch = spring[0]
    if ch in ".?":
        cnt += solve(spring[1:], nums)
    n = nums[0]
    if ch in "#?" and "." not in spring[:n] and (len(spring) == n or spring[n] in ".?"):
        cnt += solve(spring[n + 1 :], nums[1:])
    return cnt


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


def cnt(lines: list[str], fold: int = 1) -> int:
    total = 0
    for line in lines:
        spring, nums = line.strip().split()
        nums = tuple(int(n) for n in nums.split(",")) * fold
        spring = "?".join([spring] * fold)
        total += solve(spring, nums)
    return total


part1 = cnt(lines)
print(f"Part 1: {part1}")

part2 = cnt(lines, 5)
print(f"Part 2: {part2}")
