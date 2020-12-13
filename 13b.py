import fileinput
from time import sleep

for line in fileinput.input():
  if fileinput.lineno() == 1:
    time = int(line.strip())
  else:
    buses = line.strip().split(',')
    break


def first_two(n, m, step):
  i = 1
  j = 1
  while True:
    x = n * i
    y = m * j
    diff = y - x
    if diff == step:
      return (x, n * m)

    if diff > n:
      i += 1
    else:
      j += 1


def next(start, delta, n, step):
  i = 0
  while True:
    x = start + delta * i + step
    if x % n == 0:
      return x - step
    i += 1


n = int(buses.pop(0))
step = 1
m = buses.pop(0)
while m == 'x':
  step += 1
  m = buses.pop(0)
m = int(m)

start, delta = first_two(n, m, step)

while buses:
  z = buses.pop(0)
  step += 1
  while z == 'x':
    step += 1
    z = buses.pop(0)
  z = int(z)

  start = next(start, delta, z, step)
  delta *= z

print(start)