#!/usr/bin/env python3

import sys

import sympy


class Stone:
    def __init__(self, line) -> None:
        # 20, 19, 15 @  1, -5, -3
        pos, vel = line.split("@")
        self.x, self.y, self.z = list(map(int, pos.split(",")))
        self.dx, self.dy, self.dz = list(map(int, vel.split(",")))

    def __repr__(self) -> str:
        return f"<Stone {(self.x, self.y, self.z)}: {(self.dx, self.dy, self.dz)}>"

    def intersects(self, other) -> tuple | None:
        a = self.dy / self.dx
        c = -self.x * a + self.y
        b = other.dy / other.dx
        d = -other.x * b + other.y
        if a == b:
            return None
        x = (d - c) / (a - b)
        y = a * x + c
        t1 = (x - self.x) / self.dx
        t2 = (x - other.x) / other.dx
        return (t1, t2, x, y)


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

stones = [Stone(l) for l in lines]
part1 = 0
for i, s1 in enumerate(stones):
    for s2 in stones[:i]:
        result = s1.intersects(s2)
        if not result:
            continue
        t1, t2, x, y = result
        if (
            200000000000000 <= x <= 400000000000000
            and 200000000000000 <= y <= 400000000000000
            and t1 > 0
            and t2 > 0
        ):
            part1 += 1

print(f"Part 1: {part1}")


eqs = []
xr, yr, zr, dxr, dyr, dzr = sympy.symbols("xr, yr, zr, dxr, dyr, dzr")
for s in stones:
    eqs.append((s.x - xr) * (dyr - s.dy) - (s.y - yr) * (dxr - s.dx))
    eqs.append((s.x - xr) * (dzr - s.dz) - (s.z - zr) * (dxr - s.dx))

solution = sympy.solve(eqs)
part2 = solution[0][xr] + solution[0][yr] + solution[0][zr]
print(f"Part 2: {part2}")
