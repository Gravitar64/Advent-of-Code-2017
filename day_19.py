import time


def load(file):
  with open(file) as f:
    return [zeile for zeile in f.read().split('\n')]


def solve(p):
  grid = {x+1j*y: c for y, row in enumerate(p) for x, c in enumerate(row) if c != ' '}
  pos, steer, path = next(pos for pos in grid if pos.imag == 0), 0+1j, []
  
  while pos in grid:
    if grid[pos] == '+': 
      steer = next(s for s in [steer *1j, steer *-1j] if pos+s in grid)
    path.append(grid[pos])
    pos += steer  
  
  return ''.join(c for c in path if c.isalpha()), len(path)


start = time.perf_counter()
puzzle = load('day_19.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
