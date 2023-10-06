import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f.readlines()]


def solve(puzzle, steps, rules, infected=0):
  grid = {x + 1j * y: 'i' for y, row in enumerate(puzzle) for x, c in enumerate(row) if c == '#'}
  facing = 0 + -1j
  node = len(puzzle[0]) // 2 + 1j * (len(puzzle) // 2)
  
  for _ in range(steps):
    rot, new_state, add = rules[grid.get(node, 'c')]
    facing *= rot
    grid[node] = new_state
    infected += add
    node += facing
  return infected


start = time.perf_counter()
puzzle = load('day_22.txt')
p1 = dict(c=(-1j, 'i', 1), i=(1j, 'c', 0))
p2 = dict(c=(-1j, 'w', 0), w=(1, 'i', 1), i=(1j, 'f', 0), f=(-1, 'c', 0))

print(f'Part 1: {solve(puzzle, 10_000, p1)}')
print(f'Part 2: {solve(puzzle, 10_000_000, p2)}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
