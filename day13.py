# https://adventofcode.com/2015/day/13

import re
import itertools

def all_happ(ss, me):
    vs = {}
    es = {}
    for s in ss:
        m = re.fullmatch(r"([^ ]+) would (gain|lose) (\d+) happiness units by sitting next to ([^ ]+).", s)
        if not m:
            raise ValueError(f"Invalid edge: '{s}'")
        fro, sign, val, to = m.groups()
        vs[fro] = fro
        vs[to] = to
        d = int(val)
        if sign == "lose":
            d = -d
        es[(fro, to)] = int(d)
    trials = itertools.permutations(vs.keys())
    hs = []
    for t in trials:
        h = []
        for (fro, to) in itertools.pairwise(t):
            h.append(es.get((fro, to), 0))
            h.append(es.get((to, fro), 0))
        if not me:
            h.append(es.get((t[0], t[-1]), 0))
            h.append(es.get((t[-1], t[0]), 0))
        hs.append(sum(h))
    return hs

def main():
    st = open("day13_test.txt", "r").read().splitlines()
    si = open("day13_input.txt", "r").read().splitlines()
    print("max happiness test:", max(all_happ(st, False)))
    print("max happiness input:", max(all_happ(si, False)))
    print("max happiness with me test:", max(all_happ(st, True)))
    print("max happiness with me input:", max(all_happ(si, True)))

if __name__ == "__main__":
    main()
