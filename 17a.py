import fileinput

next_cells = {}


def assign(x, y, z, state):
  global next_cells
  zrow = next_cells.get(z)
  if not zrow:
    next_cells[z] = {y: {x: state}}
    return
  yrow = zrow.get(y)
  if not yrow:
    zrow[y] = {x: state}
    return
  yrow[x] = state


y = 0
for line in fileinput.input():
  for x, state in enumerate(line.strip()):
    assign(x, y, 0, state == '#')
  y += 1


def get(x, y, z):
  zrow = cur_cells.get(z)
  if not zrow:
    return False
  yrow = zrow.get(y)
  if not yrow:
    return False
  return yrow.get(x, False)


cur_cells = next_cells
next_cells = {}


def get_neighbors(x, y, z):
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1, 2):
        if i == 0 and j == 0 and k == 0:
          continue
        yield (x + i, y + j, z + k)


def living_neighbors(x, y, z):
  living = 0
  for x1, y1, z1 in get_neighbors(x, y, z):
    living += (1 if get(x1, y1, z1) else 0)
  return living


for i in range(6):
  cells_to_visit = set()
  for z, zrow in cur_cells.items():
    for y, yrow in zrow.items():
      for x, state in yrow.items():
        cells_to_visit.add((x, y, z))
        for x1, y1, z1 in get_neighbors(x, y, z):
          cells_to_visit.add((x1, y1, z1))

  for x, y, z in cells_to_visit:
    neighbors = living_neighbors(x, y, z)
    if get(x, y, z):
      if neighbors in (2, 3):
        assign(x, y, z, True)
      else:
        assign(x, y, z, False)
    else:
      if neighbors == 3:
        assign(x, y, z, True)
      else:
        assign(x, y, z, False)

  cur_cells = next_cells
  next_cells = {}

alive = 0
for z, zrow in cur_cells.items():
  for y, yrow in zrow.items():
    for x, state in yrow.items():
      alive += 1 if state else 0

print(alive)