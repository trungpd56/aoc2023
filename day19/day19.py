#!/usr/bin/env python3

import math
import sys

ops = {">": int.__gt__, "<": int.__lt__}


def apply_wf(part, namewf):
    if namewf in "AR":
        return namewf
    for category, op, num, target in wf[namewf]:
        if category == "default" or ops[op](part[category], num):
            return apply_wf(part, target)
    assert False


with open(sys.argv[1], "r") as f:
    raw_wf, raw_parts = f.read().strip().split("\n\n")

wf = {}
for line in raw_wf.splitlines():
    # px{a<2006:qkq,m>2090:A,rfg}
    name, raw_rules = line.strip("}").split("{")  # }
    rules = []
    for rule in raw_rules.split(","):
        if ":" not in rule:
            rules.append(("default", None, None, rule))
            continue
        condition, target = rule.split(":")
        category = condition[0]
        op = condition[1]
        num = int(condition[2:])
        rules.append((category, op, num, target))
    wf[name] = rules

part1 = 0
for line in raw_parts.splitlines():
    # {x=787,m=2655,a=1222,s=2876}
    vals = line.strip("{}").split(",")
    part = {}
    for val in vals:
        vtype, v = val.split("=")
        part[vtype] = int(v)
    if apply_wf(part, "in") == "A":
        part1 += sum(part.values())

print(f"Part 1: {part1}")


def apply_wf_ranges(ranges, namewf) -> int:
    if namewf == "R":
        return 0
    if namewf == "A":
        return math.prod(stop - start for start, stop in ranges.values())

    total = 0
    for cat, op, num, target in wf[namewf]:
        if cat == "default":
            total += apply_wf_ranges(ranges, target)
            continue
        start, stop = ranges[cat]
        if op == "<":
            match_rg = (start, min(num, stop))
            miss_rg = (max(num, start), stop)
        else:
            # plus 1 because it is greater not equal, with range in python it will be num-1
            match_rg = (max(num + 1, start), stop)
            miss_rg = (start, min(num + 1, stop))
        if match_rg[0] < match_rg[1]:
            next_rgs = dict(ranges)
            next_rgs[cat] = match_rg
            total += apply_wf_ranges(next_rgs, target)
        if miss_rg[0] < miss_rg[1]:
            ranges = dict(ranges)
            ranges[cat] = miss_rg
        else:
            break

    return total


part2 = apply_wf_ranges({k: (1, 4001) for k in "xmas"}, "in")
print(f"Part 2: {part2}")

