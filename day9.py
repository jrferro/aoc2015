# https://adventofcode.com/2015/day/9

import re
import itertools

def all_dists(ss):
    vs = {}
    es = {}
    for s in ss:
        m = re.fullmatch(r"([^ ]+) to ([^ ]+) = (\d+)", s)
        if not m:
            raise ValueError(f"Invalid edge: '{s}'")
        fro, to, d = m.groups()
        vs[fro] = fro
        vs[to] = to
        es[(fro, to)] = int(d)
        es[(to, fro)] = int(d)
    trials = itertools.permutations(vs.keys())
    dists = []
    for t in trials:
        path = [es[(fro, to)] for (fro, to) in itertools.pairwise(t)]
        dists.append(sum(path))
    return dists

def main():
    st = open("day9_test.txt", "r").read().splitlines()
    si = open("day9_input.txt", "r").read().splitlines()
    print("min distance test:", min(all_dists(st)))
    print("min distance input:", min(all_dists(si)))
    print("max distance test:", max(all_dists(st)))
    print("max distance input:", max(all_dists(si)))

if __name__ == "__main__":
    main()
