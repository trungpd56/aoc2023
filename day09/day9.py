#!/usr/bin/env python3

import sys


def first(nums: list[int]) -> int:
    r = 0
    for i in range(1, len(nums)):
        r = nums[i] - r
    return r


def dfs(nums: list[int], res: list[list[int]], p2: bool = False) -> int:
    if all(n == 0 for n in res[-1]):
        return 0
    nnums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    res.append(nnums)
    dfs(nnums, res, p2)
    if not p2:
        return sum(nums[-1] for nums in res)
    return first([nums[0] for nums in res[::-1]])


with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    lnums = [list(map(int, line.split())) for line in lines]

cnt = 0
for lnum in lnums:
    cnt += dfs(lnum, [lnum])
part1 = cnt
print(f"Part 1: {part1}")

cnt = 0
for lnum in lnums:
    cnt += dfs(lnum, [lnum], True)
part2 = cnt
print(f"Part 2: {part2}")
