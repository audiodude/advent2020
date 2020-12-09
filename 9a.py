import fileinput

nums = []
for line in fileinput.input():
  nums.append(int(line.strip()))


def is_sum(n, cands):
  for i, inum in enumerate(cands):
    for j in range(i, len(cands)):
      if inum + cands[j] == n:
        return True
  return False


for i, n in enumerate(nums[25:]):
  if not is_sum(n, nums[i:25 + i]):
    print(n)