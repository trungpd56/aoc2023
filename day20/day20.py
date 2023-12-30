#!/usr/bin/env python3

import sys
from collections import deque
import math


class Module:
    def __init__(self, line: str) -> None:
        # broadcaster -> a, b, c
        # %a -> b
        # &inv -> a
        raw, output = line.strip().split(" -> ")
        if raw == "broadcaster":
            self.type = "b"
            self.name = raw
            self.mem = None
        elif raw[0] == "%":
            self.type = "f"
            self.name = raw[1:]
            self.mem = 0
        elif raw[0] == "&":
            self.type = "c"
            self.name = raw[1:]
            self.mem = {}
        else:
            assert False
        self.outputs = output.split(", ")

    def __repr__(self) -> str:
        return f"<Module {(self.name, self.type)}: {self.outputs}>"


class System:
    def __init__(self, lines: list[str]) -> None:
        self.hi = 0
        self.lo = 0
        self.modules = {}
        for line in lines:
            module = Module(line)
            self.modules[module.name] = module

        for module in self.modules.values():
            for output in module.outputs:
                if output not in self.modules:
                    continue
                output_module = self.modules[output]
                if output_module.type == "c":
                    output_module.mem[module.name] = 0

    def push(self, n: int=1000, key_mods=None) -> None:
        # state: (source, hi/lo, dest)
        i = 1
        while True:
            queue = deque([("button", 0, "broadcaster")])

            while queue:
                src, pulse, dst = queue.popleft()
                if pulse == 0:
                    self.lo += 1
                else:
                    self.hi += 1

                if key_mods and src in key_mods and pulse == 1:
                    print(f"Sending {pulse} from {src} to {dst} at push{i}")
                    if not key_mods[src]:
                        key_mods[src] = i
                    if all(key_mods.values()):
                        return

                if dst not in self.modules:
                    continue
                module = self.modules[dst]
                match module.type:
                    case "b":
                        next_pulse = pulse
                    case "f":
                        if pulse == 1:
                            continue
                        module.mem = int(not module.mem)
                        next_pulse = module.mem
                    case "c":
                        module.mem[src] = pulse
                        next_pulse = 0 if all(module.mem.values()) else 1
                    case _:
                        assert False
                for output in module.outputs:
                    queue.append((module.name, next_pulse, output))
            i += 1
            if n and i > n:
                return


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

system = System(lines)
system.push()
part1 = system.lo * system.hi
print(f"Part 1: {part1}")


system2 = System(lines)
for module in system2.modules.values():
    if 'rx' in module.outputs:
        # print(f"Found module that feed rx: {module.name}")
        to_rx = module
key_mods = {}
for module in system2.modules.values():
    if to_rx.name in module.outputs:
        # print(f"Found {module.name} inputs to {to_rx.name}: {module}")
        key_mods[module.name] = None

cycle2 = system2.push(key_mods=key_mods)
part2 = math.lcm(3769,3797,3863,3931)
print(f"Part 2: {part2}")

