# https://adventofcode.com/2015/day/12

import json

def struct_sum(o):
    if isinstance(o, int):
        return o
    if isinstance(o, str):
        return 0
    if isinstance(o, dict):
        return sum([struct_sum(v) for v in o.values()])
    elif isinstance(o, list):
        return sum([struct_sum(v) for v in o])
    else:
        raise ValueError(f"Unknown structure type: {type(o)}")

def sum_json(s):
    o = json.loads(s)
    return struct_sum(o)

def struct_sum_no_red(o):
    if isinstance(o, int):
        return o
    if isinstance(o, str):
        return 0
    if isinstance(o, dict):
        if "red" in o.values():
            return 0
        else:
            return sum([struct_sum_no_red(v) for v in o.values()])
    elif isinstance(o, list):
        return sum([struct_sum_no_red(v) for v in o])
    else:
        raise ValueError(f"Unknown structure type: {type(o)}")

def sum_json_no_red(s):
    o = json.loads(s)
    return struct_sum_no_red(o)

def main():
    st = open("day12_test.txt", "r").read().strip()
    si = open("day12_input.txt", "r").read().strip()
    print("test sum:", sum_json(st))
    print("input sum:", sum_json(si))
    print("test no red sum:", sum_json_no_red(st))
    print("input no red sum:", sum_json_no_red(si))

if __name__ == "__main__":
    main()
