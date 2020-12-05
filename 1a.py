import fileinput

numbers = set()
for line in fileinput.input():
  numbers.add(int(line.strip()))

for n in numbers:
  if 2020 - n in numbers:
    print(n * (2020 - n))
    break