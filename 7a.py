from collections import defaultdict
import fileinput
import re

RE_BAG = re.compile(r'((\d+) (.+)|no other) bags?')

lookup = {}

x = []
for line in fileinput.input():
  container, contents = line.strip().split(' contain ')
  container = container[:-5]
  lookup[container] = []
  for raw_bag in contents.strip('.').split(', '):
    md = RE_BAG.match(raw_bag)
    if not md:
      print(raw_bag)
      break
    lookup[container].append((md.group(2), md.group(3)))

contained_by = defaultdict(list)
for container, contents in lookup.items():
  for c in contents:
    contained_by[c[1]].append(container)


def contained_colors(colors):
  ans = []
  for c in colors:
    ans.append(c)
    ans.extend(contained_colors(contained_by[c]))
  return ans


print(len(set(contained_colors(['shiny gold'])) - {'shiny gold'}))