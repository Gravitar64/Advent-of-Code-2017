from time import perf_counter as pfc


def load(file):
  with open(file) as f:
    return f.read().split(',')


def solve(p):
  prgs = 'a b c d e f g h i j k l m n o p'.split()
  rest = 1_000_000_000_000 % 30
  for i in range(rest):
    for e in p:
      match e[0]:
        case 's': 
          n = int(e[1:])
          prgs = prgs[-n:]+prgs[:-n]        
        
        case 'x': 
          a,b = map(int,e[1:].split('/'))
          prgs[a], prgs[b] = prgs[b], prgs[a]
        
        case 'p': 
          a,b = e[1:].split('/')
          i1,i2 = prgs.index(a), prgs.index(b)
          prgs[i1], prgs[i2] = prgs[i2], prgs[i1]
            
    if not i: part1 = ''.join(prgs)
  return part1, ''.join(prgs)  


start = pfc()
p = load('day_16.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')