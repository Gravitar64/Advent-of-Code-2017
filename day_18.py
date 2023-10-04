import time
from collections import defaultdict, deque


class Computer():
  def __init__(self, prg, part1):
    self.prg = prg
    self.pc = 0
    self.recovered = 0
    self.registers = defaultdict(int)
    self.queue = deque()
    self.part1 = part1
    self.otherComp = None
    self.sendCounter = 0
    self.waiting = False

  def step(self):
    def v(val): return self.registers[val] if val.isalpha() else int(val)

    opc, *values = self.prg[self.pc].split()
    reg, a = values[0], v(values[0])
    if len(values) == 2: b = v(values[1])
    match opc:
      case 'set': self.registers[reg] = b
      case 'add': self.registers[reg] += b
      case 'mul': self.registers[reg] *= b
      case 'mod': self.registers[reg] %= b
      case 'snd':
        self.recovered = a
        if not self.part1:
          self.otherComp.queue.append(a)
          self.sendCounter += 1
      case 'rcv':
        if self.part1 and a: return self.recovered
        if not self.part1:
          if self.queue:
            self.registers[reg] = self.queue.popleft()
            self.waiting = False
          else:
            self.waiting = True
            return
      case 'jgz':
        if a > 0:
          self.pc += b
          return
    self.pc += 1


def load(file):
  with open(file) as f:
    return [zeile.strip() for zeile in f.readlines()]


def solve(prg):
  comp, comp0, comp1 = Computer(prg, True), Computer(prg, False), Computer(prg, False)
  while True:
    if comp.step(): break

  comp0.otherComp, comp1.otherComp = comp1, comp0
  comp1.registers['p'] = 1
  while True:
    comp0.step()
    comp1.step()
    if comp0.waiting and comp1.waiting: break

  return comp.recovered, comp1.sendCounter


start = time.perf_counter()
prg = load('day_18.txt')
part1, part2 = solve(prg)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
