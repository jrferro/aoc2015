# https://adventofcode.com/2015/day/18

DIRS = [
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0]
]

def val(grid, y, x):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return 0
    return grid[y][x]

def nbr_ct(grid, y, x):
    return sum([val(grid, y+d[0], x+d[1]) for d in DIRS])

def eval_cell(grid, y, x):
    cur = val(grid, y, x)
    ct = nbr_ct(grid, y, x)
    if cur == 0 and ct == 3:
        return 1
    if cur == 1 and ct in (2, 3):
        return 1
    return 0

def next_grid(grid, stuck=False):
    g = [[eval_cell(grid, y, x) for x in range(len(grid[y]))] for y in range(len(grid))]
    if stuck:
        g[0][0] = 1
        g[0][-1] = 1
        g[-1][-1] = 1
        g[-1][0] = 1
    return g

def run_grid(g, n, stuck=False):
    for i in range(n):
        g = next_grid(g, stuck)
    return g

def on_ct(grid):
    return sum([sum(row) for row in grid])

def main():
    st = open("day18_test.txt", "r").read().splitlines()
    gt = [[1 if c == '#' else 0 for c in s] for s in st]
    si = open("day18_input.txt", "r").read().splitlines()
    gi = [[1 if c == '#' else 0 for c in s] for s in si]
    grid = run_grid(gt, 4)
    print("count test:", on_ct(grid))
    grid = run_grid(gi, 100)
    print("count input:", on_ct(grid))
    st = open("day18_test2.txt", "r").read().splitlines()
    gt = [[1 if c == '#' else 0 for c in s] for s in st]
    grid = run_grid(gt, 5, stuck=True)
    print("stuck test:", on_ct(grid))
    grid = run_grid(gi, 100, stuck=True)
    print("stuck input:", on_ct(grid))

if __name__ == "__main__":
    main()
