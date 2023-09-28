from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return [d for d in f.read().split(',')]


def solve(p):
  dist = lambda x,y,z: (abs(x) + abs(y) + abs(z)) // 2
  dirs = dict(n=(0, 1, -1), nw=(-1, 1, 0), ne=(1, 0, -1),
              sw=(-1, 0, 1), s=(0, -1, 1), se=(1, -1, 0))
  
  x = y = z = part2 = 0
  for d in p:
    dx, dy, dz = dirs[d]
    x, y, z = x + dx, y + dy, z + dz
    part2 = max(part2, dist(x, y, z))
  return dist(x, y, z), part2


start = pfc()
p = load('day_11.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
