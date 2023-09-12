from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return [z.split() for z in f.readlines()]


def solve(p):
  part1 = sum(len(set(z)) == len(z) for z in p)
  part2 = sum(len(set(''.join(sorted(e)) for e in z)) == len(z) for z in p)
  return part1, part2


start = pfc()
p = load('day_04.txt')
part1, part2 = solve(p)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')