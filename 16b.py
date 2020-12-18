from collections import defaultdict
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


def matches_range(i, r):
  return not (r[1] > i or (r[2] < i and r[3] > i) or r[4] < i)


def all_valid(n):
  ans = True
  for i in n:
    found_valid = False
    for r in ranges:
      if matches_range(i, r):
        found_valid |= True
        break
    ans &= found_valid
  return ans


valid_nearby = [n for n in nearby if all_valid(n)]

matches = defaultdict(list)
for i in range(len(valid_nearby[0])):
  for r in ranges:
    numbers_matched = list(
        map(lambda x: matches_range(x, r), [n[i] for n in valid_nearby]))
    if all(numbers_matched):
      matches[i].append(r[0])

idx_to_field = {}
f = None
while matches:
  for idx, fields in matches.items():
    if len(fields) == 1:
      f = fields[0]
      idx_to_field[idx] = f
      break

  idx_to_remove = None
  for idx, fields in matches.items():
    fields.remove(f)
    if not fields:
      idx_to_remove = idx

  del matches[idx_to_remove]

product = 1
for idx, field in idx_to_field.items():
  if 'departure' in field:
    product *= mine[idx]

print(product)