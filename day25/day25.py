#!/usr/bin/env python3

import sys
import networkx as nx

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

graph = nx.Graph()
for line in lines:
    left, right = line.split(": ")
    for node in right.split():
        graph.add_edge(left, node)

cut_value, partition = nx.stoer_wagner(graph)

part1 = len(partition[0]) * len(partition[1])
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")

