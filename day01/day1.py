#!/usr/bin/env python3

import pathlib
import sys
import regex as re

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    total = 0
    for line in data:
        chars = list(re.findall(r"\d+", line))
        if len(chars) >= 2:
            first, *_, last = chars
        else:
            first = last = chars[0]
        total += int(first[0] + last[-1])
    return total



def getval(word):
    vals = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
    try:
        return int(word)
    except ValueError:
        return int(vals[word])

def part2(data):
    """Solve part 2."""
    reg = re.compile(r"\d+|one|two|three|four|five|six|seven|eight|nine")
    total = 0
    for line in data:
        chars = reg.findall(line, overlapped=True)
        if len(chars) >= 2:
            first = getval(chars[0])
            last = getval(chars[-1])
        else:
            first = last = getval(chars[0])
        val = str(first)[0] + str(last)[-1]
        print(chars, val)
        total += int(val)
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
