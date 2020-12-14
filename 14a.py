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

mask = None
memory = {}
for cmd in cmds:
  if cmd[0] == 'mask':
    mask = cmd[1]
    continue

  b = list('{0:036b}'.format(cmd[2]))
  for i, m in enumerate(mask):
    if m == 'X':
      continue
    elif m == '1':
      b[i] = '1'
    elif m == '0':
      b[i] = '0'

  memory[cmd[1]] = int(''.join(b), 2)

print(sum(memory.values()))