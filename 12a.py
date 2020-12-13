import fileinput

instr = []
for line in fileinput.input():
  line = line.strip()
  instr.append((line[0], int(line[1:])))


class Position:
  ROT = {
      'r': {
          'n': {
              0: 'n',
              90: 'e',
              180: 's',
              270: 'w'
          },
          's': {
              0: 's',
              90: 'w',
              180: 'n',
              270: 'e'
          },
          'e': {
              0: 'e',
              90: 's',
              180: 'w',
              270: 'n'
          },
          'w': {
              0: 'w',
              90: 'n',
              180: 'e',
              270: 's'
          }
      },
      'l': {
          'n': {
              0: 'n',
              90: 'w',
              180: 's',
              270: 'e'
          },
          's': {
              0: 's',
              90: 'e',
              180: 'n',
              270: 'w'
          },
          'e': {
              0: 'e',
              90: 'n',
              180: 'w',
              270: 's'
          },
          'w': {
              0: 'w',
              90: 's',
              180: 'e',
              270: 'n'
          }
      },
  }

  def __init__(self):
    self.x = 0
    self.y = 0
    self.h = 'e'

  def n(self, u):
    self.y += u

  def s(self, u):
    self.y -= u

  def e(self, u):
    self.x += u

  def w(self, u):
    self.x -= u

  def l(self, u):
    self.h = self.ROT['l'][self.h][u]

  def r(self, u):
    self.h = self.ROT['r'][self.h][u]

  def f(self, u):
    getattr(self, self.h)(u)

  def distance(self):
    return abs(self.x) + abs(self.y)


p = Position()
for i, u in instr:
  getattr(p, i.lower())(u)

print(p.x, p.y, p.distance())