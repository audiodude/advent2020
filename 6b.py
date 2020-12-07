import fileinput

answers = []
group = []
for line in fileinput.input():
  if line == '\n':
    answers.append(group)
    group = []
    continue
  group.append(line.strip())
answers.append(group)

tally = 0
for group in answers:
  questions = []
  for person in group:
    questions.append(set(list(person)))
  tally += len(questions.pop().intersection(*questions))

print(tally)