from time import perf_counter as pfc
import collections
import re


def load(file):
  with open(file) as f:
    return f.readlines()


def dfs(node, weights, parents):
  sub = []
  for child in parents[node]:
    terminate, weight = dfs(child, weights, parents)
    if terminate: return True, weight
    sub.append(weight)
  if len(set(sub)) > 1:
    target,failure = list(collections.Counter(sub))
    return True, target - failure + weights[parents[node][sub.index(failure)]]
  return False, weights[node] + sum(sub)


def solve(p):
  weights, parents = dict(), dict()
  for z in p:
    node, n, *children = re.findall('\w+', z)
    weights[node], parents[node] = int(n), children
  part1, = set(parents) - {c for children in parents.values() for c in children}
  part2 = dfs(part1, weights, parents)
  return part1, part2


start = pfc()
p = load('day_07.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2[1]}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
