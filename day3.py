# https://adventofcode.com/2015/day/3

from collections import defaultdict

DIRS = {"^": (1, 0),
        ">": (0, 1),
        "v": (-1, 0),
        "<": (0, -1)}

def houses_solo(s):
    cur = (0, 0)
    visited = defaultdict(int)
    visited[cur] = 1
    for c in s:
        cur = (cur[0]+DIRS[c][0], cur[1]+DIRS[c][1])
        visited[cur] += 1
    return len(visited)

def houses_robot(s):
    scur = (0, 0)
    rcur = (0, 0)
    visited = defaultdict(int)
    visited[scur] += 1
    visited[rcur] += 1
    for i, c in enumerate(s):
        if i%2:
            scur = (scur[0]+DIRS[c][0], scur[1]+DIRS[c][1])
            visited[scur] += 1
        else:
            rcur = (rcur[0]+DIRS[c][0], rcur[1]+DIRS[c][1])
            visited[rcur] += 1
    return len(visited)

def main():
    s = open("day3_input.txt", "r").readline().strip()
    print("houses visited solo:", houses_solo(s))
    print("houses visited with robot:", houses_robot(s))

if __name__ == "__main__":
    main()
