from time import perf_counter as pfc


def solve():
  pos, step, buffer = 0, 314, [0]

  for value in range(1, 2018):
    pos = (pos + step) % value + 1
    buffer.insert(pos, value)
  part1 = buffer[pos + 1]

  pos = 0
  for value in range(1, 50_000_001):
    pos = (pos + step) % value + 1
    if pos == 1:  part2 = value

  return part1, part2


start = pfc()
part1, part2 = solve()
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
