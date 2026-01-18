# https://adventofcode.com/2015/day/2

def paper_needed(s):
    ds = [int(d) for d in s.split("x")]
    ds.sort()
    return 3*ds[0]*ds[1] + 2*ds[1]*ds[2] + 2*ds[2]*ds[0]

def total_paper(ss):
    return sum([paper_needed(s) for s in ss])

def ribbon_needed(s):
    ds = [int(d) for d in s.split("x")]
    ds.sort()
    return 2*(ds[0]+ds[1]) + ds[0]*ds[1]*ds[2]

def total_ribbon(ss):
    return sum([ribbon_needed(s) for s in ss])

def main():
    ss = open("day2_input.txt", "r").read().splitlines()
    print("total paper:", total_paper(ss))
    print("total ribbon:", total_ribbon(ss))

if __name__ == "__main__":
    main()
