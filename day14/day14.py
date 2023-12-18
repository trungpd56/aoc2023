#!/usr/bin/env python3

import sys


class Grid:
    def __init__(self, lines: list[str]) -> None:
        self.grid = tuple([line.strip() for line in lines])
        self.rotate_counter_clock()

    def rotate_counter_clock(self) -> None:
        self.grid = tuple(map("".join, zip(*self.grid)))[::-1]

    def rotate_clock(self) -> None:
        for _ in range(3):
            self.rotate_counter_clock()

    def display(self) -> None:
        text = "\n".join(self.grid)
        print(text)

    def tilt(self) -> None:
        self.grid = tuple(
            [
                "#".join(["".join(sorted(s, reverse=True)) for s in row.split("#")])
                for row in self.grid
            ]
        )

    def tilt_cycle(self) -> None:
        for _ in range(4):
            self.tilt()
            self.rotate_clock()

    def title_cycles(self, i: int) -> None:
        states = [self.grid]
        count = 0
        while count < i:
            self.tilt_cycle()
            count += 1
            if self.grid in states:
                break
            states.append(self.grid)
        if count == i:
            return
        first_seen = states.index(self.grid)
        cycle = count - first_seen
        self.grid = states[(i - first_seen) % cycle + first_seen]

    def score(self) -> int:
        return sum(
            len(self.grid[0]) - i
            for row in self.grid
            for i, ch in enumerate(row)
            if ch == "O"
        )


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

grid = Grid(lines)
grid.tilt()
part1 = grid.score()
print(f"Part 1: {part1}")


grid2 = Grid(lines)
grid2.title_cycles(1000000000)
part2 = grid2.score()
print(f"Part 2: {part2}")
