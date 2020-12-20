import fileinput

next_cells = {}


def assign(x, y, z, w, state):
  global next_cells
  wrow = next_cells.get(w)
  if not wrow:
    next_cells[w] = {z: {y: {x: state}}}
    return
  zrow = wrow.get(z)
  if not zrow:
    wrow[z] = {y: {x: state}}
    return
  yrow = zrow.get(y)
  if not yrow:
    zrow[y] = {x: state}
    return
  yrow[x] = state


y = 0
for line in fileinput.input():
  for x, state in enumerate(line.strip()):
    assign(x, y, 0, 0, state == '#')
  y += 1


def get(x, y, z, w):
  wrow = cur_cells.get(w)
  if not wrow:
    return False
  zrow = wrow.get(z)
  if not zrow:
    return False
  yrow = zrow.get(y)
  if not yrow:
    return False
  return yrow.get(x, False)


cur_cells = next_cells
next_cells = {}


def get_neighbors(x, y, z, w):
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1, 2):
        for m in range(-1, 2):
          if i == 0 and j == 0 and k == 0 and m == 0:
            continue
          yield (x + i, y + j, z + k, w + m)


def living_neighbors(x, y, z, w):
  living = 0
  for x1, y1, z1, w1 in get_neighbors(x, y, z, w):
    living += (1 if get(x1, y1, z1, w1) else 0)
  return living


for i in range(6):
  cells_to_visit = set()
  for w, wrow in cur_cells.items():
    for z, zrow in wrow.items():
      for y, yrow in zrow.items():
        for x, state in yrow.items():
          cells_to_visit.add((x, y, z, w))
          for x1, y1, z1, w1 in get_neighbors(x, y, z, w):
            cells_to_visit.add((x1, y1, z1, w1))

  for x, y, z, w in cells_to_visit:
    neighbors = living_neighbors(x, y, z, w)
    if get(x, y, z, w):
      if neighbors in (2, 3):
        assign(x, y, z, w, True)
      else:
        assign(x, y, z, w, False)
    else:
      if neighbors == 3:
        assign(x, y, z, w, True)
      else:
        assign(x, y, z, w, False)

  cur_cells = next_cells
  next_cells = {}

alive = 0
for w, wrow in cur_cells.items():
  for z, zrow in wrow.items():
    for y, yrow in zrow.items():
      for x, state in yrow.items():
        alive += 1 if state else 0

print(alive)