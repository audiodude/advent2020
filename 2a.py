import fileinput

valid = 0
for line in fileinput.input():
  r, letter, pwd = line.split(' ')
  low, high = map(lambda s: int(s), r.split('-'))
  letter = letter[0]
  count = pwd.count(letter)
  if low <= count and count <= high:
    valid += 1

print(valid)