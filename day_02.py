from time import perf_counter as pfc
from itertools import permutations as perm


def load(file):
  with open(file) as f:
    return [list(map(int,z.split())) for z in f.readlines()]


def solve(p):
  part1 = sum(max(z)-min(z) for z in p)
  part2 = sum(a/b for z in p for a,b in perm(z,2) if (a/b).is_integer())
  return part1, int(part2)
    

start = pfc()
puzzle = load('day_02.txt')
print(f'Part 1 & 2: {solve(puzzle)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
