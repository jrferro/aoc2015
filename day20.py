# https://adventofcode.com/2015/day/20

import sympy

def presents(n):
    ps = [10*i for i in sympy.divisors(n)]
    return sum(ps)

def min_presents(n):
    i = 1
    while (True):
        if presents(i) >= n:
            return i
        i += 1

def capped_presents(n):
    ps = [11*i for i in sympy.divisors(n) if n <= 50*i]
    return sum(ps)

def min_capped_presents(n):
    i = 1
    while (True):
        if capped_presents(i) >= n:
            return i
        i += 1

def main():
    print("min presents test:", min_presents(150))
    print("min presents input:", min_presents(36000000))
    print("min capped presents input:", min_capped_presents(36000000))

if __name__ == "__main__":
    main()
