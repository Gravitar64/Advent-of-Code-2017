import time


def load(file):
  with open(file) as f:
    return [zeile for zeile in f.read().split('\n')]


def solve(p):
  grid = {x+1j*y: c for y, row in enumerate(p) for x, c in enumerate(row) if c != ' '}
  pos, steer, path = [pos for pos in grid if pos.imag == 0][0], 0+1j, []
  
  while pos in grid:
    if grid[pos] == '+': 
      steer = [s for s in [steer *1j, steer *-1j] if pos+s in grid][0]
    path.append(pos)
    pos += steer  
  
  return ''.join(grid[pos] for pos in path if grid[pos].isalpha()), len(path)


start = time.perf_counter()
puzzle = load('day_19.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
