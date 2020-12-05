import fileinput

passports = []
passport = []
for line in fileinput.input():
  if line == '\n':
    passports.append(passport)
    passport = []
    continue
  passport.extend(map(lambda x: x.split(':'), line.strip().split(' ')))
passports.append(passport)

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid = 0
for passport in passports:
  parts = set(map(lambda x: x[0], passport))
  missing = fields - parts
  if len(missing) == 0 or (len(missing) == 1 and 'cid' in missing):
    valid += 1

print(valid)