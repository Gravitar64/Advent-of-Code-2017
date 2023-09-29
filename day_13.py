from time import perf_counter as pfc


def load(file):
  p = dict()
  with open(file) as f:
    for z in f.readlines():
      a, b = [int(n) for n in z.split(':')]
      p[a] = b
  return p


def solve(p):
  part1 = 0
  for i in p:
    if i%(2*p[i]-2): continue 
    part1 += i*p[i]

  part2 = 1
  while True:
    for i in p:
      if (i+part2)%(2*p[i]-2): continue
      break
    else:
      break
    part2 += 1

  return part1, part2


start = pfc()
p = load('day_13.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
