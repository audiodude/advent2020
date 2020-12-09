import fileinput

instr = []
for line in fileinput.input():
  parts = line.strip().split(' ')
  instr.append((parts[0], parts[1][0], int(parts[1][1:])))

seen = set()
acc = 0
i = 0
while True:
  if i in seen:
    break
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

print(acc)