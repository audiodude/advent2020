import fileinput

nums = []
for line in fileinput.input():
  nums.append(int(line.strip()))

WEAK = 217430975

i = 0
j = 1
while True:
  s = sum(nums[i:j - 1])
  if s == WEAK:
    break
  elif s < WEAK:
    j += 1
  else:
    i += 1

print(min(nums[i:j - 1]) + max(nums[i:j - 1]))