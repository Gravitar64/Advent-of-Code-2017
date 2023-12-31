from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return [int(n) for n in f.read().split()]


def solve(p):
  counter, seen, l = 0, dict(), len(p)
  while tuple(p) not in seen:
    seen[tuple(p)] = counter
    m = max(p)
    i = p.index(m)
    p[i] = 0
    for j in range(i+1,i+1+m):
      p[j%l] += 1
    counter += 1
  return counter, counter - seen[tuple(p)]


start = pfc()
p = load('day_06.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')