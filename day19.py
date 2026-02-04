# https://adventofcode.com/2015/day/19

import re

def parse(ss):
    blank = False
    rules = []
    ins = []
    for s in ss:
        if s == "":
            blank = True
        elif blank:
            ins.append(s)
        else:
            m = re.fullmatch(r"([^ ]+) => ([^ ]+)", s)
            if not m:
                raise ValueError(f"Invalid subst: {s}")
            rules.append(m.groups())
    return rules, ins

def all_subs(rule, str):
    result = set()
    for m in re.finditer(rule[0], str):
        result.add(str[:m.start()] + rule[1] + str[m.end():])
    return result

def mols(db, str):
    result = set()
    for rule in db:
        result.update(all_subs(rule, str))
    return result

# This works in theory, but the combinatorial explosion of BFS prevents it from
# working in practice.  This problem probably needs a parser.
def build_time(db, ins, goal):
    if goal in ins:
        return 0
    nexts = set.union(*[mols(db, i) for i in ins])
    return 1 + build_time(db, nexts, goal)

def revdb(db):
    return [(r[1], r[0]) for r in db]

def main():
    st = open("day19_test.txt", "r").read().splitlines()
    dbt, inst = parse(st)
    si = open("day19_input.txt", "r").read().splitlines()
    dbi, insi = parse(si)
    print("calibration tests:")
    for i in inst:
        print(i, ":", len(mols(dbt, i)))
    print("calibration inputs:")
    for i in insi:
        print(i, ":", len(mols(dbi, i)))
    print("building tests:")
    for i in inst:
        print(i, ":", build_time(dbt, ["e"], i))
    for i in inst:
        print(i, ":", build_time(revdb(dbt), [i], "e"))
    print("building inputs:")
    for i in insi:
        print(i, ":", build_time(dbi, ["e"], i))
    for i in insi:
        print(i, ":", build_time(revdb(dbi), [i], "e"))

if __name__ == "__main__":
    main()
