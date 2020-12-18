import fileinput

section = 0
ranges = []
mine = None
nearby = []
for line in fileinput.input():
  if line == '\n':
    section += 1
    continue

  if section == 0:
    word, rest = line.strip().split(':')
    range1, range2 = rest[1:].split(' or ')
    a, b = [int(n) for n in range1.split('-')]
    c, d = [int(n) for n in range2.split('-')]
    ranges.append((word, a, b, c, d))
    continue

  if section == 1:
    if line.strip() == 'your ticket:':
      continue
    mine = [int(n) for n in line.strip().split(',')]
    continue

  if section == 2:
    if line.strip() == 'nearby tickets:':
      continue

    nearby.append([int(n) for n in line.strip().split(',')])


def invalid_values(n):
  ans = set()
  for i in n:
    found_valid = False
    for r in ranges:
      if not (r[1] > i or (r[2] < i and r[3] > i) or r[4] < i):
        found_valid |= True
        break
    if not found_valid:
      ans.add(i)
  return ans


all_invalid = []
for n in nearby:
  all_invalid.extend(invalid_values(n))

print(sum(all_invalid))