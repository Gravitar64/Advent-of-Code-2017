import time
import re
from collections import defaultdict


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('-?\d+', zeile))) for zeile in f.readlines()]


def add_vector(v1, v2):
  return [a + b for a, b in zip(v1, v2)]


def new_pos(values):
    p, v, a = values[:3], values[3:6], values[6:]
    v = add_vector(v, a)
    p = add_vector(p, v)
    return p+v+a


def manhatten_dist(v1):
  return sum(abs(v) for v in v1)


def solve(puzzle):
  puzzle2 = puzzle.copy()
  for _ in range(500):
    for i, particle in enumerate(puzzle):
      puzzle[i] = new_pos(particle)

  _, particle = sorted((manhatten_dist(values), values) for values in puzzle)[0]
  part1 = puzzle.index(particle)

  for _ in range(100):
    positions = defaultdict(list)
    for i, particle in enumerate(puzzle2):
      particle = new_pos(particle)
      puzzle2[i] = particle
      positions[tuple(particle[:3])].append(particle)
    
    for dupicles in positions.values():
      if len(dupicles) == 1: continue
      for dupicle in dupicles:
        puzzle2.remove(dupicle)      

  return part1, len(puzzle2)




start = time.perf_counter()
puzzle = load('day_20.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
