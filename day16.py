# https://adventofcode.com/2015/day/16

import re
import operator

Q = {
    "children": (3, operator.eq),
    "cats": (7, operator.gt),
    "samoyeds": (2, operator.eq),
    "pomeranians": (3, operator.lt),
    "akitas": (0, operator.eq),
    "vizslas": (0, operator.eq),
    "goldfish": (5, operator.lt),
    "trees": (3, operator.gt),
    "cars": (2, operator.eq),
    "perfumes": (1, operator.eq),
}

def fill_db(ss):
    db = {}
    for s in ss:
        m = re.fullmatch(r"Sue (\d+): ([^ ]+): (\d+), ([^ ]+): (\d+), ([^ ]+): (\d+)", s)
        if not m:
            raise ValueError(f"Invalid db string: 's'")
        n, p1, c1, p2, c2, p3, c3 = m.groups()
        db[n] = {p1: int(c1), p2: int(c2), p3: int(c3)}
    return db

def find_aunt(q, db, use_ops=False):
    for aunt, props in db.items():
        found = True
        for n, c in props.items():
            v, op = q[n]
            if not use_ops:
                op = operator.eq
            if not op(c, v):
                found = False
        if found:
            return aunt

def main():
    ss = open("day16_db.txt", "r").read().splitlines()
    db = fill_db(ss)
    print("matching aunt:", find_aunt(Q, db))
    print("matching real aunt:", find_aunt(Q, db, use_ops=True))

if __name__ == "__main__":
    main()
