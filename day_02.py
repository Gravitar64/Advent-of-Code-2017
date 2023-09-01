from time import perf_counter as pfc
from itertools import combinations as comb


def load(file):
  with open(file) as f:
    return [sorted([int(n) for n in z.split()],reverse=True) for z in f.readlines()]


def solve(p):
  part1 = sum(z[0]-z[-1] for z in p)
  part2 = sum(a//b for z in p for a,b in comb(z,2) if (a/b).is_integer())
  return part1, part2
    

start = pfc()
puzzle = load('day_02.txt')
print(f'Part 1 & 2: {solve(puzzle)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
