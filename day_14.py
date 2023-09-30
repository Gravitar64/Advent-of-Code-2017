from time import perf_counter as pfc
from functools import reduce
from operator import xor


def knot_hash(data):
  size, loop = 256, 64
  circ_list = list(range(size))
  data = [ord(c) for c in data] + [17, 31, 73, 47, 23]
  pos = skip = 0
  for _ in range(loop):
    for lenght in data:
      sequence = []
      for i in range(pos, pos + lenght):
        sequence.append(circ_list[i % size])
      for i, n in zip(range(pos, pos + lenght), reversed(sequence)):
        circ_list[i % size] = n
      pos = (pos + lenght + skip) % size
      skip += 1
  return ''.join(f'{reduce(xor,circ_list[i:i+16]):08b}' for i in range(0, size, 16))


def bfs(grid):
  used_pos = {(i % 128, i // 128) for i, n in enumerate(grid) if n}
  regions = 0
  while used_pos:
    queue = [used_pos.pop()]
    regions += 1
    while queue:
      x, y = queue.pop()
      for new_pos in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
        if new_pos not in used_pos: continue
        queue.append(new_pos)
        used_pos.remove(new_pos)
  return regions


def solve(p):
  grid = [int(bit) for i in range(128) for bit in knot_hash(f'{p}-{i}')]
  return sum(grid), bfs(grid)


start = pfc()
part1, part2 = solve('nbysizxe')
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
