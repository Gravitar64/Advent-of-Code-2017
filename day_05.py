from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return [int(z) for z in f.readlines()]


def solve(p,part1):
  pc, counter,l = 0,0,len(p)
  while pc < l:
    j = p[pc]
    p[pc] += 1 if part1 else 1 if j <3  else -1
    pc += j
    counter += 1
  return counter  
    

start = pfc()
p = load('day_05.txt')

print(f'Part 1: {solve(p.copy(),True)}')
print(f'Part 2: {solve(p,False)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')