from time import perf_counter as pfc


def solve(a, b):
  part1 = part2 = 0
  bit_mask, mod = 65536, 2147483647
  aas, bbs = [], []
  for _ in range(40_000_000):
    a, b = (a * 16807) % mod, (b * 48271) % mod
    part1 += (ma := a % bit_mask) == (mb := b % bit_mask)
    if not a % 4: aas.append(ma)
    if not b % 8: bbs.append(mb)

  for ma, mb in zip(aas[:5_000_000], bbs[:5_000_000]):
    part2 += ma == mb

  return part1, part2


start = pfc()
part1, part2 = solve(289, 629)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
