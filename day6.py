# https://adventofcode.com/2015/day/6

import re

BOOL_FUNCS = {"turn on": lambda b: True,
              "turn off": lambda b: False,
              "toggle": lambda b: not b}

def bool_lights(ss):
    grid = [[False for i in range(1000)] for i in range(1000)]
    insn = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")
    for s in ss:
        m = insn.fullmatch(s)
        if not m:
            raise ValueError
        (func_name, x0, y0, x1, y1) = m.groups()
        func = BOOL_FUNCS[func_name]
        for x in range(int(x0), int(x1)+1):
            for y in range (int(y0), int(y1)+1):
                grid[y][x] = func(grid[y][x])
    return sum([line.count(True) for line in grid])

ELF_FUNCS = {"turn on": lambda b: b+1,
             "turn off": lambda b: b-1 if b>=1 else 0,
             "toggle": lambda b: b+2}

def elf_lights(ss):
    grid = [[0 for i in range(1000)] for i in range(1000)]
    insn = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")
    for s in ss:
        m = insn.fullmatch(s)
        if not m:
            raise ValueError
        (func_name, x0, y0, x1, y1) = m.groups()
        func = ELF_FUNCS[func_name]
        for x in range(int(x0), int(x1)+1):
            for y in range (int(y0), int(y1)+1):
                grid[y][x] = func(grid[y][x])
    return sum([sum(line) for line in grid])

def main():
    ss = open("day6_input.txt", "r").read().splitlines()
    print("boolean brightness:", bool_lights(ss))
    print("elvish brightness:", elf_lights(ss))

if __name__ == "__main__":
    main()
