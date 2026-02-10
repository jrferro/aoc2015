# https://adventofcode.com/2015/day/23

from attrs import define, field
import re

@define
class mach():
    code: list = field(factory=list)
    regs: dict = field(factory=dict)
    ip: int = 0

    @classmethod
    def from_code(cls, code):
        m = mach()
        m.code = [i for i in code]
        m.reinit()
        return m
    
    def reinit(self):
        self.regs['a'] = 0
        self.regs['b'] = 0
        self.ip = 0
    
    def sim(self):
        self.reinit()
        while self.ip < len(self.code):
            self.exec_one()

    def exec_one(self):
        insn = self.code[self.ip]
        args = insn.split()
        if len(args) == 3:
            args[1] = args[1].strip(',')
        match args[0]:
            case "hlf":
                self.regs[args[1]] //= 2
            case "tpl":
                self.regs[args[1]] *= 3
            case "inc":
                self.regs[args[1]] += 1
            case "jmp":
                self.ip += int(args[1]) - 1
            case "jie":
                if self.regs[args[1]] % 2 == 0:
                    self.ip += int(args[2]) - 1
            case "jio":
                if self.regs[args[1]] == 1:
                    self.ip += int(args[2]) - 1
            case _:
                raise ValueError(f"Invalid insn: {insn}")
        self.ip += 1

def main():
    code_test = open("day23_test.txt", "r").read().splitlines()
    mt = mach.from_code(code_test)
    mt.sim()
    print("After test, a =", mt.regs['a'])
    code_input = open("day23_input.txt", "r").read().splitlines()
    mi = mach.from_code(code_input)
    mi.sim()
    print("After input, b =", mi.regs['b'])
    mi.code = ["inc a"] + mi.code
    mi.sim()
    print("After input starting with a = 1, b =", mi.regs['b'])

if __name__ == "__main__":
    main()
