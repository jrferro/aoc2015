# https://adventofcode.com/2015/day/8

def size_diff(s):
    l = 0
    i = 0
    while i < len(s):
        if s[i] == '\"' and (i == 0 or i == len(s) - 1):
            l -= 1
        elif s[i] == '\\' and (s[i+1] == '"' or s[i+1] == '\\'):
            i += 1
        elif s[i] == '\\' and s[i+1] == 'x':
            i += 3
        else:
            pass
        l += 1
        i += 1
    return len(s) - l

def reencode_diff(s):
    l = 0
    i = 0
    while i < len(s):
        if s[i] == '\"' and (i == 0 or i == len(s) - 1):
            l += 2
        elif s[i] == '\\' and (s[i+1] == '"' or s[i+1] == '\\'):
            l += 3
            i += 1
        elif s[i] == '\\' and s[i+1] == 'x':
            l += 1
        else:
            pass
        l += 1
        i += 1
    return l - len(s)

def main():
    st = open("day8_test.txt", "r").read().splitlines()
    si = open("day8_input.txt", "r").read().splitlines()
    print("test size diff:", sum([size_diff(s) for s in st]))
    print("input size diff:", sum([size_diff(s) for s in si]))
    print("test reencode diff:", sum([reencode_diff(s) for s in st]))
    print("input reencode diff:", sum([reencode_diff(s) for s in si]))

if __name__ == "__main__":
    main()
