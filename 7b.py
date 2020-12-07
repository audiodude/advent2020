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


def num_bags(color):
  ans = 0
  for n, bag in lookup[color]:
    if n is None and bag is None:
      continue
    ans += int(n) * (num_bags(bag) + 1)
  return ans


print(num_bags('shiny gold'))