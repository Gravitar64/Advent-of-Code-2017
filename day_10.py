from time import perf_counter as pfc
from functools import reduce
from operator import xor


def load(file):
  with open(file) as f:
    return f.readline().strip()


def solve(p, size, part1=True):
  circ_list = list(range(size))
  pos = skip = 0

  if part1:
    loops = 1
    puzzle = [int(n) for n in p.split(',')]
  else:
    loops = 64
    puzzle = [ord(c) for c in p] + [17, 31, 73, 47, 23]

  for _ in range(loops):
    for lenght in puzzle:
      sequence = []
      for i in range(pos, pos + lenght):
        sequence.append(circ_list[i % size])
      for i, n in zip(range(pos, pos + lenght), reversed(sequence)):
        circ_list[i % size] = n
      pos = (pos + lenght + skip) % size
      skip += 1

  if part1: return circ_list[0] * circ_list[1]
  return ''.join(f'{reduce(xor,circ_list[i:i+16]):02x}' for i in range(0, size, 16))


start = pfc()
p = load('day_10.txt')
print(f'Part 1: {solve(p,256)}')
print(f'Part 2: {solve(p, 256, False)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
