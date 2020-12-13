import fileinput

for line in fileinput.input():
  if fileinput.lineno() == 1:
    time = int(line.strip())
  else:
    buses = line.strip().split(',')
    break

buses = [int(b) for b in buses if b != 'x']

t = 0
ans = None
while True:
  for b in buses:
    if (time + t) % b == 0:
      ans = b * t
      break
  if ans is not None:
    print(ans)
    break
  t += 1