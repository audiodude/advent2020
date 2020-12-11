import fileinput

cur_rows = []
for line in fileinput.input():
  cur_rows.append(list(line.strip()))

NUM_COLS = len(line)
NUM_ROWS = len(cur_rows)


def is_floor(char):
  return char == '.'


def is_empty(char):
  return char == 'L'


def is_full(char):
  return char == '#'


def neighboring_coords(x, y):
  for i in range(-1, 2):
    if x + i < 0 or x + i >= NUM_ROWS:
      continue
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if y + j < 0 or y + j >= NUM_COLS:
        continue
      yield (x + i, y + j)


def num_neighbors(x, y):
  n = 0
  for x, y in neighboring_coords(x, y):
    if is_full(cur_rows[x][y]):
      n += 1
  return n


next_rows = [[None] * NUM_COLS for x in range(NUM_ROWS)]
while True:
  for x, row in enumerate(cur_rows):
    for y, seat in enumerate(row):
      if is_empty(seat):
        if num_neighbors(x, y) == 0:
          next_rows[x][y] = '#'
        else:
          next_rows[x][y] = 'L'
      elif is_full(seat):
        if num_neighbors(x, y) >= 4:
          next_rows[x][y] = 'L'
        else:
          next_rows[x][y] = '#'
      elif is_floor(seat):
        next_rows[x][y] = '.'
      else:
        raise ValueError((x, y, cur_rows[x][y], row, seat, num_neighbors(x, y)))

  found_diff = False
  for x in range(NUM_ROWS):
    for y in range(NUM_COLS):
      if next_rows[x][y] != cur_rows[x][y]:
        found_diff = True
        break
    if found_diff:
      break
  if not found_diff:
    break

  cur_rows = next_rows
  next_rows = [[None] * NUM_COLS for x in range(NUM_ROWS)]

count = 0
for row in next_rows:
  for seat in row:
    if seat == '#':
      count += 1

print(count)