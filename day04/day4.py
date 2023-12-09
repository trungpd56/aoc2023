#!/usr/bin/env python3

import pathlib
from collections import defaultdict
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.splitlines():
        parts = line.split(" | ")
        nums = list(map(int, re.findall(r"\d+", parts[0])))
        id_ = nums[0]
        win = set(nums[1:])
        cards = set(map(int, re.findall(r"\d+", parts[1])))
        data.append((id_, win, cards))
    return data


def part1(data):
    """Solve part 1."""
    score = 0
    for parts in data:
        diff = parts[1] & parts[2]
        if (l := len(diff)) > 0:
            score += 2 ** (l - 1)
    return score


def part2(data):
    """Solve part 2."""
    cards = defaultdict(int)
    for parts in data:
        l = len(parts[1] & parts[2])
        idn = parts[0]
        cards[idn] += 1
        if l > 0:
            for n in range(idn + 1, idn + l + 1):
                cards[n] += cards[idn]
    return sum(cards.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    infile = (
        sys.argv[1]
        if len(sys.argv) > 1
        else pathlib.Path(__file__).parent / "input.txt"
    )
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
