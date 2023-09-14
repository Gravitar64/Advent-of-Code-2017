from time import perf_counter as pfc
import collections
import re


def load(file):
  with open(file) as f:
    return f.readlines()


def dfs(node, weights, childs):
  global part2
  sub = [dfs(c, weights, childs) for c in childs[node]]
  if not part2 and len(set(sub)) > 1:
    (target, _), (failure, _) = collections.Counter(sub).most_common()
    part2 = target - failure + weights[childs[node][sub.index(failure)]]
  return weights[node] + sum(sub)


def solve(p):
  weights, childs = dict(), dict()
  for z in p:
    node, n, *children = re.findall('\w+', z)
    weights[node] = int(n)
    childs[node] = tuple(children)
  part1, = set(childs) - {child for children in childs.values()
                          for child in children}
  dfs(part1, weights, childs)
  return part1


start = pfc()
p = load('day_07.txt')
part2 = None
part1 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
