# https://adventofcode.com/2015/day/5

import re

def is_nice_1(s):
    vowel_check = re.search(r"[aeiou].*[aeiou].*[aeiou]", s)
    pair_check = re.search(r"(.)\1", s)
    naughty_check = re.search(r"ab|cd|pq|xy", s)
    return bool(vowel_check and pair_check and not naughty_check)

def is_nice_2(s):
    double_pair_check = re.search(r"(..).*\1", s)
    uwu_check = re.search(r"(.).\1", s)
    return bool(double_pair_check and uwu_check)

def main():
    ss = open("day5_input.txt", "r").read().splitlines()
    print("nice 1 strings:", len([s for s in ss if is_nice_1(s)]))
    print("nice 2 strings:", len([s for s in ss if is_nice_2(s)]))

if __name__ == "__main__":
    main()
