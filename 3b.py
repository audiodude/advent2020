import fileinput

def total(slope_x, slope_y):
  x = 0
  y = 0
  count = 0
  while y < len(trees):
    count += 1 if trees[y][x % len(trees[y])] == '#' else 0
    x += slope_x
    y += slope_y

  return count

trees = []
for line in fileinput.input():
  trees.append(line.strip())

print(total(1, 1) * total(3, 1) * total(5, 1) * total(7, 1) * total(1, 2))