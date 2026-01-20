# https://adventofcode.com/2015/day/14

import re

def build_rates(ss, t):
    racers = {}
    for s in ss:
        m = re.fullmatch(r"([^ ]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", s)
        if not m:
            raise ValueError(f"Invalid racer: '{s}'")
        name, rate, run, rest = m.groups()
        racers[name] = [int(rate)] * int(run) + [0] * int(rest)
        while len(racers[name]) < t:
            racers[name] = racers[name] * 2
    return racers

def dists(ss, t):
    racers = build_rates(ss, t)
    return [sum(v[:t]) for v in racers.values()]

def points(ss, t):
    racers = build_rates(ss, t)
    dists = {}
    for h, v in racers.items():
        dists[h] = [sum(v[:i+1]) for i in range(len(v))]
    points = {h: [] for h in dists}
    for i in range(t):
        lead = max([dists[h][i] for h in dists])
        for h in points:
            if dists[h][i] == lead:
                points[h].append(1)
            else:
                points[h].append(0)
    return [sum(v[:t]) for v in points.values()]

def main():
    st = open("day14_test.txt", "r").read().splitlines()
    si = open("day14_input.txt", "r").read().splitlines()
    tt = 1000
    ti = 2503
    print(f"win distance after {tt} test:", max(dists(st, tt)))
    print(f"win distance after {ti} input:", max(dists(si, ti)))
    print(f"win points after {tt} test:", max(points(st, tt)))
    print(f"win points after {ti} input:", max(points(si, ti)))

if __name__ == "__main__":
    main()
