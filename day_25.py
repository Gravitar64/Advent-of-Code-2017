import time
import re


def load(file):
  with open(file) as f:
    return [block for block in f.read().split('\n\n')]


def solve(p):
  turingMachines = {}
  for block in p:
    states = [c[0] for c in re.findall('[A-Z]+[.:]', block)]
    numbers = list(map(int, re.findall('\d+', block)))
    rl = re.findall('right|left', block)
    if len(states) == 1:
      machine = states[0]
      steps = numbers[0]
    else:
      turingMachines[states[0]] = {0: (numbers[1], rl[0], states[1]), 
                                   1: (numbers[3], rl[1], states[2])}

  cursor, tape = 0, set()
  for _ in range(steps):
    write, direction, machine = turingMachines[machine][0 if cursor not in tape else 1]
    if write:
      tape.add(cursor)
    elif cursor in tape: 
      tape.remove(cursor)
    cursor += 1 if direction == 'right' else -1
  return len(tape)


start = time.perf_counter()
prg = load('day_25.txt')
print(f'Part 1: {solve(prg)}')
print(f'Ermittelt in {time.perf_counter()-start:.5f} Sek.')