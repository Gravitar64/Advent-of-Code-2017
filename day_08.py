from time import perf_counter as pfc
import collections


def load(file):
  with open(file) as f:
    return f.readlines()


def solve(p):
  registers = collections.defaultdict(int)
  part2 = 0
  for z in p:
    register, command, n, _, *condition = z.split()
    condition[0] = f'registers.get("{condition[0]}",0)'
    if eval(' '.join(condition)):
      registers[register] += int(n) if command == 'inc' else -int(n)
    part2 = max(part2, max(registers.values()))
  return max(registers.values()), part2


start = pfc()
p = load('day_08.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')