# https://adventofcode.com/2015/day/4

import hashlib

def lowest_coin(s, d):
    i = 0
    while True:
        h = hashlib.md5()
        h.update(bytes(s+str(i), "utf-8"))
        if h.hexdigest()[:d] == '0' * d:
            return i
        i += 1

def main():
    d = 5
    s = "abcdef"
    print(f"{d} coin for {s}:", lowest_coin(s, d))
    s = "pqrstuv"
    print(f"{d} coin for {s}:", lowest_coin(s, d))
    s = "ckczppom"
    print(f"{d} coin for {s}:", lowest_coin(s, d))
    d = 6
    print(f"{d} coin for {s}:", lowest_coin(s, d))

if __name__ == "__main__":
    main()
