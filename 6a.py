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
  questions = set()
  for person in group:
    for letter in person:
      questions.add(letter)
  tally += len(questions)

print(tally)
