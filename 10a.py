import fileinput

adapters = []
for line in fileinput.input():
  adapters.append(int(line.strip()))

adapters.sort()
adapters.append(adapters[-1] + 3)

last = 0
ones = 0
threes = 0
for a in adapters:
  if a - 1 == last:
    ones += 1
  elif a - 3 == last:
    threes += 1
  last = a

print(ones, threes, ones * threes)