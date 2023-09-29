from time import perf_counter as pfc
import re
import networkx as nx


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', zeile))) for zeile in f.readlines()]


def solve(p):
  g = nx.Graph()
  for node, *neighbors in p:
    g.add_edges_from((node, neighbor) for neighbor in neighbors)
  return len(nx.node_connected_component(g, 0)), nx.number_connected_components(g)


start = pfc()
p = load('day_12.txt')
part1, part2 = solve(p)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Ermittelt in {pfc()-start:.5f} Sek.')
