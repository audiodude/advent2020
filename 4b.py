import fileinput
import re

passports = []
passport = []
for line in fileinput.input():
  if line == '\n':
    passports.append(passport)
    passport = []
    continue
  passport.extend(map(lambda x: x.split(':'), line.strip().split(' ')))
passports.append(passport)

RE_HGT = re.compile(r'(\d+)(cm|in)')
RE_HCL = re.compile(r'#[a-f0-9]{6}')
ECL = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
RE_PID = re.compile(r'\d+')


def is_valid(passport):
  parts = set(map(lambda x: x[0], passport))
  missing = fields - parts
  if not (len(missing) == 0 or (len(missing) == 1 and 'cid' in missing)):
    return False
  for field, value in passport:
    try:
      year = int(value)
    except ValueError:
      year = 0
    if field == 'byr':
      if not (len(value) == 4 and year >= 1920 and year <= 2002):
        return False
    elif field == 'iyr':
      if not (len(value) == 4 and year >= 2010 and year <= 2020):
        return False
    elif field == 'eyr':
      if not (len(value) == 4 and year >= 2020 and year <= 2030):
        return False
    elif field == 'hgt':
      md = RE_HGT.match(value)
      if not md:
        return False
      else:
        try:
          hgt = int(md.group(1))
        except ValueError:
          hgt = 0
        if md.group(2) == 'cm' and not (hgt >= 150 and hgt <= 193):
          return False
        elif md.group(2) == 'in' and not (hgt >= 59 and hgt <= 76):
          return False
    elif field == 'hcl':
      md = RE_HCL.match(value)
      if md is None:
        return False
    elif field == 'ecl':
      if value not in ECL:
        return False
    elif field == 'pid':
      md = RE_PID.match(value)
      if md is None or len(value) != 9:
        return False
    elif field == 'cid':
      pass
    else:
      return False

  return True


fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid = 0
for passport in passports:
  if is_valid(passport):
    valid += 1

print(valid)