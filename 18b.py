import fileinput

exprs = []
for line in fileinput.input():
  exprs.append(line.strip())


class Expression:

  def __init__(self, data):
    self.evaluated = None
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
    if self.evaluated is not None:
      return self.evaluated

    all_plus_done = False
    for i in range(2):
      lnum = None
      lnum_idx = None
      opr = None
      i = 0
      while i < len(self.data):
        c = self.data[i]
        if c == ' ':
          i += 1
          continue

        if lnum is None:
          getlnum = self._get_num(i, c)
          lnum = getlnum[0]
          lnum_idx = i
          i = getlnum[1]
        elif opr is None:
          opr = c
        else:
          rnum = self._get_num(i, c)
          if opr == '+':
            s = lnum + rnum[0]
            self.data = self.data[:lnum_idx] + '%s' % s + self.data[rnum[1]:]
            i = lnum_idx - 1
            lnum = None
          elif opr == '*' and all_plus_done:
            lnum *= rnum[0]
            i = rnum[1]
          else:
            lnum = rnum[0]
            lnum_idx = i
            i = rnum[1]
          opr = None
        i += 1
      all_plus_done = True

    self.evaluated = lnum
    return lnum

  def _get_num(self, i, c):
    last_idx = self.data.find(' ', i)
    end = last_idx if last_idx != -1 else len(self.data)
    if c == '#':
      if last_idx == -1:
        id_ = int(self.data[i + 2:])
      else:
        id_ = int(self.data[i + 2:last_idx])

      try:
        return (self.sub[id_].evaluate(), end)
      except KeyError:
        print(self.data, id_)
        raise
    else:
      if last_idx == -1:
        num = int(self.data[i:])
      else:
        num = int(self.data[i:last_idx])
      return (num, end)


s = 0
for expr in exprs:
  x = Expression(expr)
  s += x.evaluate()

print(s)