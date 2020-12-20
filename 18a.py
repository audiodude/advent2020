import fileinput

exprs = []
for line in fileinput.input():
  exprs.append(line.strip())


class Expression:

  def __init__(self, data):
    self.simple = None
    self.sub = {}
    self.sub_id = 0
    self.data = data

    idx = self.data.find('(')
    if idx == -1:
      self.simple = self.data
      return

    start = None
    while True:
      parens = []
      start = None
      for i, c in enumerate(self.data):
        if c != '(' and c != ')':
          continue
        if c == '(':
          if not parens:
            start = i
          parens.append(True)
        else:
          parens.pop()
          if not parens:
            stop = i
            break

      if start is None:
        break

      self.sub[self.sub_id] = Expression(self.data[start + 1:stop])
      self.data = self.data[:start] + '#s%s' % self.sub_id + self.data[stop +
                                                                       1:]
      self.sub_id += 1

  def __repr__(self):
    return self.data

  def evaluate(self):
    lnum = None
    opr = None
    i = 0
    while i < len(self.data):
      c = self.data[i]
      if c == ' ':
        i += 1
        continue

      if lnum is None:
        lnum = self._get_num(i, c)
      elif opr is None:
        opr = c
      else:
        rnum = self._get_num(i, c)
        if opr == '+':
          lnum += rnum
        elif opr == '*':
          lnum *= rnum
        opr = None
      i += 1

    return lnum

  def _get_num(self, i, c):
    if c == '#':
      last_idx = self.data.find(' ', i)
      if last_idx == -1:
        id_ = int(self.data[i + 2:])
      else:
        id_ = int(self.data[i + 2:last_idx])
      return self.sub[id_].evaluate()
    else:
      return int(c)


s = 0
for expr in exprs:
  x = Expression(expr)
  s += x.evaluate()

print(s)