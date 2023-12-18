#!/usr/bin/env python3

import sys
from collections import defaultdict


class Seq:
    def __init__(self, line: str) -> None:
        self.toks = line.split(",")

    def badhash(self, tok: str) -> int:
        cur = 0
        for c in tok:
            cur = ((cur + ord(c)) * 17) % 256
        return cur

    def run(self) -> int:
        return sum(self.badhash(t) for t in self.toks)

    def run2(self):
        boxes = defaultdict(list)
        info = defaultdict(int)
        for tok in self.toks:
            if "=" in tok:
                k, val = tok.split("=")
                if k not in boxes[self.badhash(k)]:
                    boxes[self.badhash(k)].append(k)
                info[k] = int(val)
            elif "-" in tok:
                k = tok.strip("-")
                if k in boxes[self.badhash(k)]:
                    boxes[self.badhash(k)].remove(k)
            else:
                assert False
        total = 0
        for n, box in boxes.items():
            total += sum((n + 1) * i * info[k] for i, k in enumerate(box, 1))
        return total


with open(sys.argv[1], "r") as f:
    line = f.read().strip()

seq = Seq(line)
part1 = seq.run()
print(f"Part 1: {part1}")

part2 = seq.run2()
print(f"Part 2: {part2}")
