import fileinput

orig_instr = []
for line in fileinput.input():
  parts = line.strip().split(' ')
  orig_instr.append((parts[0], parts[1][0], int(parts[1][1:])))


def test(instr):
  seen = set()
  acc = 0
  i = 0
  while True:
    if i in seen:
      return None
    if i == len(instr):
      return acc
    seen.add(i)

    cmd, sign, val = instr[i]
    if cmd == 'nop':
      i += 1
    elif cmd == 'acc':
      if sign == '+':
        acc += val
      elif sign == '-':
        acc -= val
      else:
        raise ValueError((instr[i], i))
      i += 1
    elif cmd == 'jmp':
      if sign == '+':
        i += val
      elif sign == '-':
        i -= val
      else:
        raise ValueError((instr[i], i))


for i, cur in enumerate(orig_instr):
  if cur[0] == 'jmp':
    res = test(orig_instr[:i] + [('nop', cur[1], cur[2])] + orig_instr[i + 1:])
    if res is not None:
      break
  elif cur[0] == 'nop':
    res = test(orig_instr[:i] + [('jmp', cur[1], cur[2])] + orig_instr[i + 1:])
    if res is not None:
      break
  elif cur[0] == 'acc':
    pass
  else:
    raise ValueError(cur)

print(res)
