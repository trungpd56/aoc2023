#!/usr/bin/env python3

import sys
import re
from math import prod


def solve(t, time, dist):
    return (time - t) * t > dist


with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    rtimes = list(map(int, re.findall(r"\d+", lines[0])))
    rdist = list(map(int, re.findall(r"\d+", lines[1])))
    races = [(t, d) for t, d in zip(rtimes, rdist)]

res = []
for race in races:
    time, dist = race
    cnt = 0
    t = 1
    while t <= time:
        cnt += solve(t, time, dist)
        t += 1
    res.append(cnt)


part1 = prod(res)
print(f"Part 1: {part1}")


time = int("".join(map(str, rtimes)))
dist = int("".join(map(str, rdist)))
t = 1
cnt = 0
while t < time:
    while t <= time:
        cnt += solve(t, time, dist)
        t += 1


part2 = cnt
print(f"Part 2: {part2}")
