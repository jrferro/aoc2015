# https://adventofcode.com/2015/day/10

def lns(s):
    acc = ""
    while len(s) > 0:
        i = 0
        c = s[0]
        while (i < len(s) and s[i] == c):
            i += 1
        acc += str(i) + c
        s = s[i:]
    print(len(acc))
    return acc

def lns_seq(s, n):
    ss = [s]
    while n > 0:
        ss.append(lns(ss[-1]))
        n -= 1
    return ss

def main():
    st = "1"
    si = "1113122113"
    print("length test after 4:", len(lns_seq(st, 4)[-1]))
    print("length input after 40:", len(lns_seq(si, 40)[-1]))
    print("length input after 50:", len(lns_seq(si, 50)[-1]))

if __name__ == "__main__":
    main()
