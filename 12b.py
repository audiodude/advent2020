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

  def __init__(self, with_ship=True):
    self.x = 10
    self.y = 1
    if with_ship:
      self.ship = Position(with_ship=False)
      self.ship.x = 0
      self.ship.y = 0

  def n(self, u):
    self.y += u

  def s(self, u):
    self.y -= u

  def e(self, u):
    self.x += u

  def w(self, u):
    self.x -= u

  def l(self, u):
    if u == 0:
      pass
    elif u == 180:
      self.x *= -1
      self.y *= -1
    elif u == 90:
      tmp = self.x
      self.x = -1 * self.y
      self.y = tmp
    elif u == 270:
      tmp = self.x
      self.x = self.y
      self.y = -1 * tmp

  def r(self, u):
    if u == 0:
      pass
    elif u == 180:
      self.x *= -1
      self.y *= -1
    elif u == 90:
      tmp = self.x
      self.x = self.y
      self.y = -1 * tmp
    elif u == 270:
      tmp = self.x
      self.x = -1 * self.y
      self.y = tmp

  def f(self, u):
    self.ship.x += self.x * u
    self.ship.y += self.y * u

  def distance(self):
    return abs(self.x) + abs(self.y)


p = Position()
for i, u in instr:
  getattr(p, i.lower())(u)

print(p.ship.x, p.ship.y, p.ship.distance())