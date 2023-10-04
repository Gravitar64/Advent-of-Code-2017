import time
import re


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('-?\d+', zeile))) for zeile in f.readlines()]


def add_vector(v1, v2):
  return [a + b for a, b in zip(v1, v2)]


def manhatten_dist(v1):
  return sum(abs(v) for v in v1)


def solve(puzzle):
  puzzle2 = puzzle.copy()
  for _ in range(600):
    for i, values in enumerate(puzzle):
      p, v, a = values[:3], values[3:6], values[6:]
      v = add_vector(v, a)
      p = add_vector(p, v)
      puzzle[i] = p + v + a

  _, values = sorted((manhatten_dist(values), values) for values in puzzle)[0]
  part1 = puzzle.index(values)

  for _ in range(600):
    to_del, positions = set(), set()
    for i, values in enumerate(puzzle2):
      p, v, a = values[:3], values[3:6], values[6:]
      v = add_vector(v, a)
      p = add_vector(p, v)
      puzzle2[i] = p + v + a
      if tuple(p) in positions:
        to_del.add(tuple(p))
      else:
        positions.add(tuple(p))
    puzzle2 = [values for values in puzzle2 if not tuple(
      values[0:3]) in to_del]

  return part1, len(puzzle2)


start = time.perf_counter()
puzzle = load('day_20.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
