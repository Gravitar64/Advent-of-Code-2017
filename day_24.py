import time


def load(file):
  with open(file) as f:
    return [list(map(int, line.split("/"))) for line in f]


def solve(path,comps,last):
  strongest, longest = path, path
  for i,c in enumerate(comps):
    if last not in c: continue
    strong, long = solve(path+c, comps[:i]+comps[i+1:], c[0] if c[1] == last else c[1])
    if sum(strong) > sum(strongest): strongest = strong
    if len(long) >= len(longest) and sum(long) > sum(longest): longest = long
  return strongest, longest  

  
start = time.perf_counter()
puzzle = load('day_24.txt')
part1, part2 = solve([],puzzle,0)
print(f'Part 1: {sum(part1)}')
print(f'Part 2: {sum(part2)}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')
