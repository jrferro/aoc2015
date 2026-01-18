# https://adventofcode.com/2015/day/1

def find_floor(s):
    f = 0
    for c in s:
        if c == "(":
            f += 1
        elif c == ")":
            f -= 1
        else:
            raise NotImplementedError
    return f

def find_basement(s):
    f = 0
    for i, c in enumerate(s):
        if c == "(":
            f += 1
        elif c == ")":
            f -= 1
            if f < 0:
                return i + 1
        else:
            raise NotImplementedError
    raise IndexError

def main():
    s = open("day1_input.txt", "r").readline().strip()
    print("floor:", find_floor(s))
    print("first basement floor:", find_basement(s))

if __name__ == "__main__":
    main()
