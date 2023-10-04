import time
from collections import defaultdict


class Computer():
  def __init__(self, prg):
    self.prg = prg
    self.pc = 0
    self.recovered = 0
    self.registers = defaultdict(int)
    self.queue = list()
    self.otherComp = None
    self.sendCounter = 0
    self.waiting = False

  def step(self, part1):
    def v(val): return self.registers[val] if val.isalpha() else int(val)

    opc, *values = self.prg[self.pc].split()
    reg, a = values[0], v(values[0])
    if len(values) == 2: b = v(values[1])
    
    match opc:
      case 'set': self.registers[reg] = b
      case 'add': self.registers[reg] += b
      case 'mul': self.registers[reg] *= b
      case 'mod': self.registers[reg] %= b
      case 'jgz':
        if a > 0:
          self.pc += b
          return
      case 'snd':
        self.recovered = a
        if not part1:
          self.otherComp.queue.append(a)
          self.sendCounter += 1
      case 'rcv':
        if part1 and a: return True
        if self.queue:
          self.registers[reg] = self.queue.pop(0)
          self.waiting = False
        else:
          self.waiting = True
          return
      
    self.pc += 1


def load(file):
  with open(file) as f:
    return [zeile.strip() for zeile in f.readlines()]


def solve(prg):
  comp, comp0, comp1 = Computer(prg), Computer(prg), Computer(prg)
  while True:
    if comp.step(True): break

  comp0.otherComp, comp1.otherComp = comp1, comp0
  comp1.registers['p'] = 1
  while True:
    comp0.step(False)
    comp1.step(False)
    if comp0.waiting and comp1.waiting: break

  return comp.recovered, comp1.sendCounter


start = time.perf_counter()
prg = load('day_18.txt')
part1, part2 = solve(prg)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
