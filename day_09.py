from time import perf_counter as pfc


def load(file):
    with open(file) as f:
        return f.readlines()[0]


def solve(p):
  group_score = part1 = part2 = 0
  garbage = ignore = False
  for c in p:
    if ignore:
      ignore = False
      continue
    if c == '{' and not garbage:
      group_score += 1
    elif c == '}' and not garbage:
      part1 += group_score
      group_score -= 1
    elif c == '<' and not garbage:
      garbage = True
    elif c == '!':
      ignore = True
    elif c == '>':
      garbage = False
    elif garbage:
      part2 += 1
  return part1, part2


start = pfc()
p = load('day_09.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
