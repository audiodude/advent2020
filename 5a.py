import fileinput

passes = []
for line in fileinput.input():
  passes.append(line.strip())


def s(low, high, command):
  if command == '':
    return low
  range = (high - low) // 2
  if command[0] == 'F' or command[0] == 'L':
    return s(low, low + range, command[1:])
  elif command[0] == 'B' or command[0] == 'R':
    return s(low + range + 1, high, command[1:])


nums = []
for pass_ in passes:
  row = s(0, 127, pass_[:7])
  seat = s(0, 7, pass_[8:])
  nums.append(row * 8 + seat)

print(max(nums))