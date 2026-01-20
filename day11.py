# https://adventofcode.com/2015/day/11

import re

def valid_pass(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    m = re.search(r"(.)\1.*(.)\2", s)
    if not m:
        return False
    if m.group(1) == m.group(2):
        return False
    for i in range(len(s) - 2):
        if ord(s[i])+1 == ord(s[i+1]) and ord(s[i])+2 == ord(s[i+2]):
            return True
    return False

def incr_pass(s):
    e = s[-1]
    if e == 'z':
        return incr_pass(s[:-1]) + 'a'
    else:
        return s[:-1] + chr(ord(e)+1)

def next_pass(s):
    s = incr_pass(s)
    while not valid_pass(s):
        s = incr_pass(s)
    return s

def main():
    s = "abcdefgh"
    print("next pass after", s, ":", next_pass(s))
    s = "ghijklmn"
    print("next pass after", s, ":", next_pass(s))
    s = "hepxcrrq"
    print("next pass after", s, ":", next_pass(s))
    s = next_pass(s)
    print("next pass after", s, ":", next_pass(s))

if __name__ == "__main__":
    main()
