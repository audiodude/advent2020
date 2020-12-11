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


def north(x, y):
  while y > 0:
    y -= 1
    yield (x, y)


def south(x, y):
  while y < NUM_COLS - 1:
    y += 1
    yield (x, y)


def east(x, y):
  while x < NUM_ROWS - 1:
    x += 1
    yield (x, y)


def west(x, y):
  while x > 0:
    x -= 1
    yield (x, y)


def northwest(x, y):
  while x > 0 and y > 0:
    x -= 1
    y -= 1
    yield (x, y)


def northeast(x, y):
  while x < NUM_ROWS - 1 and y > 0:
    x += 1
    y -= 1
    yield (x, y)


def southeast(x, y):
  while x < NUM_ROWS - 1 and y < NUM_COLS - 1:
    x += 1
    y += 1
    yield (x, y)


def southwest(x, y):
  while x > 0 and y < NUM_COLS - 1:
    x -= 1
    y += 1
    yield (x, y)


def num_neighbors(x, y):
  n = 0
  for gen in (north, south, east, west, northwest, northeast, southeast,
              southwest):
    for next_x, next_y in gen(x, y):
      try:
        if is_full(cur_rows[next_x][next_y]):
          n += 1
          break
        elif is_empty(cur_rows[next_x][next_y]):
          break
      except IndexError:
        print(next_x, next_y)
        raise

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
        if num_neighbors(x, y) >= 5:
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