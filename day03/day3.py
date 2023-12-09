#!/usr/bin/env python3

import pathlib
import sys
import re
import math


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def valid(pos, data):
    neis = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1,-1), (1, 0), (1, 1)]
    for r, c in pos:
        for dr, dc in neis:
            try:
                val = data[r+dr][c+dc]
                if val != '.' and not val.isdigit():
                    return True
            except IndexError:
                continue
    return False


def part1(data):
    """Solve part 1."""
    nums = []
    for row, line in enumerate(data):
        matches = re.finditer(r'\d+', line)
        for m in matches:
            pos = [(row, c) for c in range(m.start(), m.end())]
            if valid(pos, data):
                nums.append(int(m.group()))
    return sum(nums)


def find(r, c, data):
    neis = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1,-1), (1, 0), (1, 1)]
    nums = []
    for dr in (-1, 0, 1):
        matches = re.finditer(r'\d+', data[r+dr])
        for m in matches:
            pos = [(r+dr, c) for c in range(m.start(), m.end())]
            region = [(r+dr, c+dc) for dr, dc in neis]
            if any((rr, cc) in region for rr, cc in pos):
                nums.append(int(m.group()))
    return math.prod(nums) if len(nums) > 1 else 0



def part2(data):
    """Solve part 2."""
    total = 0
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == '*':
                nums = find(r, c, data)
                total += nums
    return total


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
