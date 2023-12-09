#!/usr/bin/env python3

import pathlib
import sys
from dataclasses import dataclass
from collections import defaultdict
from itertools import batched


@dataclass(frozen=True)
class Batch:
    red: int = 0
    blue: int = 0
    green: int = 0

    def valid(self, other):
        return self.red <= other.red and self.blue <= other.blue and self.green <= other.green


def parse(puzzle_input):
    """Parse input."""
    games = defaultdict(list)
    for line in puzzle_input.splitlines():
        parts = line.split(": ")
        idn = int(parts[0].split()[-1].strip(":"))
        for b in parts[1].split("; "):
            t = b.replace(",", "").split()
            games[idn].append(Batch(**{c[1]: int(c[0]) for c in batched(t, 2)}))
    return games


def part1(data):
    """Solve part 1."""
    cnt = 0
    bst = Batch(red=12, green=13, blue=14)
    for idn, batchs in data.items():
        if any(b.valid(bst) is False for b in batchs):
            continue
        cnt += idn
    return cnt


def part2(data):
    """Solve part 2."""
    cnt = 0
    for batchs in data.values():
        mred = max(b.red for b in batchs)
        mblue = max(b.blue for b in batchs)
        mgreen = max(b.green for b in batchs)
        cnt += mred * mblue * mgreen
    return cnt


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent / "input.txt"
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
