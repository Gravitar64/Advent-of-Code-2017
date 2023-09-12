from time import perf_counter as pfc
import math


def solve(p):
  circle = math.ceil(math.sqrt(p)) // 2
  circle_zero = (circle * 2 - 1)**2
  centers = [circle_zero + x * circle for x in [1, 3, 5, 7] ]
  return circle + min([abs(p - x) for x in centers ])

  
def solve2(p):
  x,y = 1,0
  vals = {(0,0):1, (x,y):1}
  while vals[(x,y)] <= p:
    x,y = next_coord(x,y)
    vals[(x,y)] = sum(vals.get((x+i, y+j), 0) for i in [-1,0,1] for j in [-1,0,1])
  return vals[(x,y)]    

  
def next_coord(x,y):
  if y >  -x  and x >  y:  return x,y+1
  if y >  -x  and y >= x:  return x-1,y
  if y <= -x  and x <  y:  return x,y-1
  return x+1,y 


start = pfc()
p = 368078
print(f'Part 1: {solve(p)}')
print(f'Part 2: {solve2(p)}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')