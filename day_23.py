import time
from collections import defaultdict
from sympy import isprime


class Computer():
  def __init__(self, prg, part):
    self.prg = prg
    self.part = part
    self.pc = 0
    self.registers = defaultdict(int)
    self.mulCounter = 0

  def run(self):
    self.registers['a'] = self.part - 1
    def v(val): return self.registers[val] if val.isalpha() else int(val)
    while self.pc < 11:
      opc, reg, val = self.prg[self.pc].split()
      val = v(val)
      match opc:
        case 'set': self.registers[reg] = val
        case 'sub': self.registers[reg] -= val
        case 'mul':
          self.registers[reg] *= val
          self.mulCounter += 1
        case 'jnz':
          if v(reg) != 0:
            self.pc += val
            continue
      self.pc += 1


def load(file):
  with open(file) as f:
    return [zeile.strip() for zeile in f.readlines()]


def solve(prg, part):
  c = Computer(prg, part)
  c.run()
  if part == 1:
    return (c.registers['b'] - c.registers['e']) * (c.registers['b'] - c.registers['d'])
  else:
    return sum(not isprime(b) for b in range(c.registers['b'], c.registers['c'] + 1, 17))


start = time.perf_counter()
prg = load('day_23.txt')
print(f'Part 1: {solve(prg,1)}')
print(f'Part 2: {solve(prg,2)}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
