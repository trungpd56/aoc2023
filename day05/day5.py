#!/usr/bin/env python3

import sys


class Range:
    def __init__(self, src: int, rg: int) -> None:
        self.low = src
        self.high = src + rg - 1

    def __repr__(self) -> str:
        return f"Range: {self.low}--{self.high}"


class Tran:
    def __init__(self, src: int, dst: int, rg: int) -> None:
        self.low = src
        self.high = src + rg - 1
        self.offset = src - dst

    def __repr__(self) -> str:
        return f"{self.low}||{self.high}||{self.offset}"

    def run(self, num) -> int | None:
        if self.low <= num <= self.high:
            return num - self.offset
        return None


class Map:
    def __init__(self, lines: list[str]) -> None:
        self.trans = []
        for line in lines[1:]:
            dst, src, rg = map(int, line.split())
            self.trans.append(Tran(src, dst, rg))

    def __repr__(self) -> str:
        return "  ".join(str(t) for t in self.trans)

    def run(self, num):
        for t in self.trans:
            if next_num := t.run(num):
                return next_num
        return num

    def run2(self, seed_ranges: list[Range]):
        ranges = [s for s in seed_ranges]
        res_ranges = []
        while ranges:
            seedrg = ranges.pop()
            for t in self.trans:
                over_low = max(seedrg.low, t.low)
                over_high = min(seedrg.high, t.high)
                if over_low < over_high:
                    res_ranges.append(Range(over_low - t.offset, over_high - over_low))
                    if seedrg.low < over_low:
                        ranges.append(Range(seedrg.low, over_low - seedrg.low))
                    if seedrg.high > over_high:
                        ranges.append(Range(over_high, seedrg.high - over_high))
                    break
            else:
                res_ranges.append(seedrg)
        return res_ranges


class Almanac:
    def __init__(self, parts: list[str]) -> None:
        self.seeds = [int(t) for t in parts[0].split() if t.isdigit()]
        self.ranges = [
            Range(*map(int, t)) for t in zip(*(iter(parts[0].split()[1:]),) * 2)
        ]
        self.maps = []
        for p in parts[1:]:
            lines = p.split("\n")
            self.maps.append(Map(lines))

    def solve(self) -> dict:
        results = {}
        for seed in self.seeds:
            res = seed
            for m in self.maps:
                res = m.run(res)
            results[seed] = res
        return results

    def solve2(self) -> list[Range]:
        ranges = [r for r in self.ranges]
        for m in self.maps:
            ranges = m.run2(ranges)
        return ranges


with open(sys.argv[1], "r") as f:
    parts = f.read().strip().split("\n\n")
    almanac = Almanac(parts)


part1 = min(almanac.solve().values())
print(f"Part 1: {part1}")

part2 = min(r.low for r in almanac.solve2())
print(f"Part 2: {part2}")
