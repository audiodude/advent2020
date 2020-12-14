import fileinput

cmds = []
for line in fileinput.input():
  cmd, val = line.strip().split(' = ')
  if cmd == 'mask':
    cmds.append((cmd, val))
  else:
    idxr = cmd.find('[')
    idxl = cmd.find(']')
    cmds.append(('mem', int(cmd[idxr + 1:idxl]), int(val)))


def floating(b):
  try:
    idx = b.index('X')
  except ValueError:
    yield b
    return
  for s in floating(b[idx + 1:]):
    yield b[:idx] + ['0'] + s
    yield b[:idx] + ['1'] + s


mask = None
memory = {}
for cmd in cmds:
  if cmd[0] == 'mask':
    mask = cmd[1]
    continue

  b = list('{0:036b}'.format(cmd[1]))
  for i, m in enumerate(mask):
    if m == '0':
      continue
    elif m == 'X':
      b[i] = 'X'
    elif m == '1':
      b[i] = '1'

  for address in floating(b):
    n = int(''.join(address), 2)
    memory[n] = cmd[2]

print(sum(memory.values()))