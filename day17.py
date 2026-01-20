# https://adventofcode.com/2015/day/17

import struct
import numpy

test = [20, 15, 10, 5, 5]
input = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

def combos(lst, target):
    found = []
    for att in range(1 << len(lst)):
        tot = []
        for i in range(len(lst)):
            if att & (1 << i):
                tot.append(lst[i])
        if sum(tot) == target:
            found.append(tot)
    return found

def main():
    ct = combos(test, 25)
    ci = combos(input, 150)
    print("combos test:", len(ct))
    print("combos input:", len(ci))
    mint = min([len(t) for t in ct])
    mini = min([len(t) for t in ci])
    print("combos min test:", len([t for t in ct if len(t) == mint]))
    print("combos min input:", len([t for t in ci if len(t) == mini]))    

if __name__ == "__main__":
    main()
