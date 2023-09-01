from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return f.read()


def solve(p, n):
  return sum(int(p[i]) for i in range(l) if p[i] == p[(i+n) % l])


start = pfc()
puzzle = load('day_01.txt')
l, n = len(puzzle), len(puzzle)//2

print(f'Part1: {solve(puzzle,1)}')
print(f'Part2: {solve(puzzle,n)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
