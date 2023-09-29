from time import perf_counter as pfc
import re
from collections import defaultdict


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', zeile))) for zeile in f.readlines()]


def solve(p):
  pipes = dict()
  for pipe in p:
    pipes[pipe[0]] = set(pipe[1:])
  all_numbers = set(n for z in p for n in z)
  groups = defaultdict(set)
  for n in range(max(all_numbers) + 1):
    queue = [n]
    while queue:
      prog = queue.pop()
      for prog2 in pipes[prog]:
        if prog2 not in all_numbers: continue
        groups[n].add(prog2)
        queue.append(prog2)
        all_numbers.remove(prog2)
  return len(groups[0]), len(groups)


start = pfc()
p = load('day_12.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
