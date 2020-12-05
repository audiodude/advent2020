import fileinput

trees = []
for line in fileinput.input():
  trees.append(line.strip())

x = 0
y = 0
count = 0
while y < len(trees):
  count += 1 if trees[y][x % len(trees[y])] == '#' else 0
  y += 1
  x += 3

print(count)