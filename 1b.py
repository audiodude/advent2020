import fileinput

numbers = set()
for line in fileinput.input():
  numbers.add(int(line.strip()))

found_numbers = False
for n in numbers:
  for m in numbers:
    if 2020 - n - m in numbers:
      print(n * m * (2020 - n - m))
      found_numbers = True
      break
  if found_numbers:
    break