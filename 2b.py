import fileinput

valid = 0
for line in fileinput.input():
  r, letter, pwd = line.split(' ')
  low, high = map(lambda s: int(s), r.split('-'))
  letter = letter[0]
  if (pwd[low - 1] == letter) != (pwd[high - 1] == letter):
    valid += 1

print(valid)