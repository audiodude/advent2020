import fileinput
from functools import reduce
import operator

adapters = []
for line in fileinput.input():
  adapters.append(int(line.strip()))

adapters.sort()
adapters.append(adapters[-1] + 3)

last = 0
ones = 0
threes = 0
chains = []
for a in adapters:
  if a - 1 == last:
    ones += 1
  elif a - 3 == last:
    chains.append(ones)
    ones = 0
  last = a

MAP = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}

print(reduce(operator.mul, map(lambda x: MAP[x], chains), 1))

# 0 3 4 5 6 7 10
# 0 3 4 5 7 10
# 0 3 4 6 7 10
# 0 3 4 7 10
# 0 3 5 6 7 10
# 0 3 6 7 10
# 0 3 5 7 10