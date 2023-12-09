#!/usr/bin/env python3

import sys
from collections import Counter


class Hand:

    def __init__(self, line, p2=False):
        toks = line.split()
        self.cards = list(toks[0])
        self.bid = int(toks[1])
        self.p2 = p2

    def __repr__(self):
        return f"{str(self.cards)}-{self.bid}"


    @property
    def power(self):
        cnt = Counter(self.cards)
        if self.p2 and 'J' in self.cards:
            skey = sorted(cnt, key=lambda x: cnt[x], reverse=True)
            if len(skey) == 1:
                pass
            else:
                maxk = skey[0] if skey[0] != 'J' else skey[1]
                cnt[maxk] += cnt['J']
                cnt['J'] = 0
        cnt = list(cnt.values())

        # five kind
        if 5 in cnt:
            return 5
        # four kind
        elif 4 in cnt:
            return 4
        # full house
        elif cnt.count(3) == 1 and cnt.count(2) == 1:
            return 3
        # three kind
        elif cnt.count(3) == 1 and cnt.count(1) == 2:
            return 2
        #two pair
        elif cnt.count(2) == 2:
            return 1
        # one pair
        elif cnt.count(2) == 1 and cnt.count(1) == 3:
            return 0
        # high card
        elif cnt.count(1) == 5:
            return -1
        else:
            assert False

    def __lt__(self, other):
        if not self.p2:
            vals = [str(n) for n in range(2,10)] + list("TJQKA")
        else:
            vals = ['J'] + [str(n) for n in range(2,10)] + list("TQKA")

        if self.power == other.power:
            i = 0
            while self.cards[i] == other.cards[i]:
                i += 1
            return vals.index(self.cards[i]) < vals.index(other.cards[i])
        return self.power < other.power



with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    hands = [Hand(line) for line in lines]
    hands2 = [Hand(line, p2=True) for line in lines]

hands.sort()
part1 = sum(h.bid*i for i, h in enumerate(hands,1))
print(f'Part 1: {part1}')

hands2.sort()
part2 = sum(h.bid*i for i, h in enumerate(hands2,1))
print(f'Part 2: {part2}')
