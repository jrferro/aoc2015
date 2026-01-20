# https://adventofcode.com/2015/day/15

import re
import numpy
import functools
import operator

def recipe_value(ingrs, amts):
    ingrs = numpy.array(ingrs).transpose()
    amts = numpy.array(amts)
    vs = ingrs @ amts
    if any([v <= 0 for v in vs]):
        return 0, 0
    return functools.reduce(operator.mul, vs[:-1], 1), vs[-1]

def read_ingrs(ss):
    ingrs = {}
    ingr_mat = []
    for s in ss:
        m = re.fullmatch(r"([^ ]+): capacity ([-\d]+), durability ([-\d]+), flavor ([-\d]+), texture ([-\d]+), calories ([-\d]+)", s)
        if not m:
            raise ValueError(f"Invalid ingredient: '{s}'")
        g = m.groups()
        ingrs[g[0]] = g[1:]
        ingr_mat.append([int(w) for w in g[1:]])
    return ingr_mat

def recipe_score_2(ss, cals=0):
    ingr_mat = read_ingrs(ss)
    vals = []
    for i in range(100 + 1):
        j = 100 - i
        v, c = recipe_value(ingr_mat, [i, j])
        if cals == 0 or c <= cals:
            vals.append(v)
    return max(vals)

def recipe_score_4(ss, cals=0):
    ingr_mat = read_ingrs(ss)
    vals = []
    for i in range(100 + 1):
        for j in range(100 - i + 1):
            for k in range(100 - i - j + 1):
                l = 100 - i - j - k
                v, c = recipe_value(ingr_mat, [i, j, k, l])
                if cals == 0 or c <= cals:
                    vals.append(v)
    return max(vals)

def main():
    st = open("day15_test.txt", "r").read().splitlines()
    si = open("day15_input.txt", "r").read().splitlines()
    print("best recipe score test:", recipe_score_2(st))
    print("best recipe score input:", recipe_score_4(si))
    print("best diet recipe score test:", recipe_score_2(st, 500))
    print("best diet recipe score input:", recipe_score_4(si, 500))

if __name__ == "__main__":
    main()
