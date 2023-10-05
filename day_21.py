import time
import numpy as np


def load(file):
  with open(file) as f:
    return f.readlines()


def str2Array(s):
  return np.array([[c == '#' for c in line] for line in s.split('/')])


def enhance_rules_with_flip_rot(rules):
  mappings = {}
  for line in rules:
    k, v = map(str2Array, line.strip().split(' => '))
    for a in (k, np.fliplr(k)):
      for r in range(4):
        mappings[np.rot90(a, r).tobytes()] = v
  return mappings


def enhance(grid, rules):
  old_size, old_by = len(grid), 2 if not len(grid) % 2 else 3
  new_size, new_by = old_size * (old_by + 1) // old_by, old_by + 1
  squares, new_squares = range(0, old_size, old_by), range(0, new_size, new_by)
  solution = np.empty((new_size, new_size), dtype=bool)

  for i, ni in zip(squares, new_squares):
    for j, nj in zip(squares, new_squares):
      square = grid[i:i + old_by, j:j + old_by]
      enhanced = rules[square.tobytes()]
      solution[ni:ni + new_by, nj:nj + new_by] = enhanced
  return solution


def solve(rules):
  rules = enhance_rules_with_flip_rot(rules)
  grid = str2Array('.#./..#/###')
  for i in range(18):
    grid = enhance(grid, rules)
    if i == 4: part1 = int(grid.sum())
  return part1, int(grid.sum())


start = time.perf_counter()
puzzle = load('day_21.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')