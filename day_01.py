from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return f.read()


def solve(p,l):
  part1 =  sum(int(p[i]) for i in range(l) if p[i] == p[(i+1) % l])
  part2 =  sum(int(p[i]) for i in range(l) if p[i] == p[(i+l//2) % l])
  return part1, part2


start = pfc()
puzzle = load('day_01.txt')
print(f'Part 1 & 2: {solve(puzzle,len(puzzle))}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
