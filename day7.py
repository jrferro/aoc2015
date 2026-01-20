# https://adventofcode.com/2015/day/7

import attrs
import re

WIDTH = 16
BITS = (1 << WIDTH) - 1

@attrs.define
class Wire:
    name: str
    value: int = 0
    ready: bool = False
    outs: list["Gate"] = attrs.field(factory=list, repr=False)

    def add_out(self, g):
        self.outs.append(g)
    
    def set_value(self, v):
        self.value = v
        self.ready = True

GATE_FUNCS = {
    "CONST": lambda ins: ins[0].value,
    "AND": lambda ins: ins[0].value & ins[1].value,
    "OR": lambda ins: ins[0].value | ins[1].value,
    "NOT": lambda ins: (~ins[0].value) & BITS,
    "LSHIFT": lambda ins: (ins[0].value << ins[1].value) & BITS,
    "RSHIFT": lambda ins: (ins[0].value >> ins[1].value) & BITS,
}

@attrs.define
class Gate:
    func: str
    ins: list[Wire]
    out: Wire

    def is_ready(self):
        return all(w.ready for w in self.ins)
    
    def value(self):
        if not self.is_ready():
            raise ValueError(f"Gate for {self.out} not ready")
        return GATE_FUNCS[self.func](self.ins)
    
    def eval(self):
        self.out.set_value(self.value())
        return [g for g in self.out.outs if g.is_ready()]

@attrs.define
class Circuit:
    wires: dict[str, Wire] = attrs.field(factory=dict)
    gates: dict[str, Gate] = attrs.field(factory=dict)

    def add_wire(self, s):
        m = re.fullmatch(r"(\d+)", s)
        if m:
            s = "C"+s
        if s not in self.wires:
            w = Wire(s)
            if m:
                w.set_value(int(m.group(1)))
            self.wires[s] = w
        return self.wires[s]
    
    def add_gate(self, f, ins, out):
        g = Gate(f, ins, out)
        if out.name in self.gates:
            raise ValueError(f"Multiply driven output: {out.name}")
        self.gates[out.name] = g
        for w in ins:
            w.add_out(g)
        return g

    def parse_gate(self, s):
        m = re.fullmatch(r"(.*) -> ([a-z]+)", s)
        if not m:
            raise ValueError(f"Invalid assignment: {s}")
        gatestr, out = m.groups()
        wout = self.add_wire(out)
        m = re.fullmatch(r"([^ ]+)", gatestr)
        if m:
            f, val = "CONST", m.group(1)
            win = self.add_wire(val)
            self.add_gate(f, [win], wout)
            return
        m = re.fullmatch(r"(NOT) ([^ ]+)", gatestr)
        if m:
            f, val = m.groups()
            win = self.add_wire(val)
            self.add_gate(f, [win], wout)
            return
        m = re.fullmatch(r"([^ ]+) (AND|OR|LSHIFT|RSHIFT) ([^ ]+)", gatestr)
        if m:
            val1, f, val2 = m.groups()
            win1 = self.add_wire(val1)
            win2 = self.add_wire(val2)
            self.add_gate(f, [win1, win2], wout)
            return
        raise ValueError(f"Invalid gate expr: {gatestr}")

    def eval(self):
        q = [g for g in self.gates.values() if g.is_ready()]
        while q:
            g = q[0]
            q = g.eval() + q[1:]

def main():
    ss = open("day7_test.txt", "r").read().splitlines()
    c = Circuit()
    for s in ss:
        c.parse_gate(s)
    c.eval()
    print("test status:", [(w.name, w.value) for w in c.wires.values()])
    ss = open("day7_input.txt", "r").read().splitlines()
    c = Circuit()
    for s in ss:
        c.parse_gate(s)
    c.eval()
    print("input status 1:", c.wires["a"])
    v = c.wires["a"].value
    c = Circuit()
    for s in ss:
        m = re.search("-> b$", s)
        if m:
            continue
        c.parse_gate(s)
    c.parse_gate(f"{v} -> b")
    c.eval()
    print("input status 2:", c.wires["a"])

if __name__ == "__main__":
    main()
