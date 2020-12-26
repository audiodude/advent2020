import fileinput

section = 0
rules = {}
tests = []
for line in fileinput.input():
  line = line.strip()
  if line == '':
    section += 1
    continue

  if section == 0:
    rule_no, rule = line.split(':')
    rule_no = int(rule_no)
    parts = rule[1:].split(' | ')
    if len(parts) == 1:
      idx = parts[0].find('"')
      if idx == -1:
        rules[rule_no] = tuple(map(int, parts[0].split(' ')))
      else:
        rules[rule_no] = tuple(parts[0][idx + 1:parts[0].find('"', idx + 1)])
    else:
      rules[rule_no] = ('|', tuple(map(int, parts[0].split(' '))),
                        tuple(map(int, parts[1].split(' '))))
  elif section == 1:
    tests.append(line)

calculated = {}


def match(test, rule):
  print('&', test, rule)
  if len(rule) == 0:
    return 0
  if len(test) == 0 and len(rule) > 0:
    print('test is empty')
    return None

  if isinstance(rule[0], str) and rule[0] == '|':
    r = tuple(rule)
  else:
    r = rule[0]

  if isinstance(r, str):
    if r == '|':
      raise ValueError()
    if test[0] != r:
      return None
    else:
      cur = 1
  elif isinstance(r, tuple):
    if r[0] == '|':
      nchars = 0
      cur = None
      for part in r[1:]:
        print('or part is', part)
        cur = match(test, part)
        if cur is not None:
          break
      else:
        return None
    else:
      nchars = 0
      for part in r:
        print('part is', part)
        rest = match(test[nchars:], part)
        if rest is None:
          return None
        nchars += rest
      cur = nchars

  rest = match(test[cur:], rule[1:])
  if rest is None:
    return None
  return cur + rest


def sub(i):
  if isinstance(i, str):
    return i
  if isinstance(i, int):
    precalc = calculated.get(i)
    if precalc:
      return precalc
    else:
      calc = tuple([sub(j) for j in rules[i]])
      if len(calc) == 1:
        calc = calc[0]
      calculated[i] = calc
      return calc
  if isinstance(i, tuple):
    val = tuple([sub(x) for x in i])
    if len(val) == 1:
      val = val[0]
    return val


calculated[0] = [sub(i) for i in rules[0]]
act = calculated[0]

n = 0
for test in tests:
  md = match(test, act)
  print(test, md)
  print()
  if md == len(test):
    n += 1

print(n)
