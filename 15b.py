from collections import defaultdict
import fileinput

for line in fileinput.input():
  nums = [int(n) for n in line.strip().split(',')]

spots = defaultdict(list)
for i, n in enumerate(nums):
  spots[n].append(i)

nums.append(0)
spots[0].append(len(nums) - 1)
i = len(nums)
while i < 30000000:
  spot = spots.get(nums[-1])
  if spot is None or len(spot) < 2:
    new = 0
  else:
    new = spot[-1] - spot[-2]
  nums.append(new)
  spots[new].append(i)
  i += 1

print(new)