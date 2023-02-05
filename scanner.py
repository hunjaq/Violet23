questions = []
qtexts = []
answers = []

with open("question.txt") as f:
    for line in f:
        qtexts.append(line.strip())


with open("answers.txt", errors="ignore") as g:
    for line2 in g:
        answers.append(line2.strip())

for i in range(len(qtexts)):
    questions[i] = question(self)
    questions[i].setQuestion(qtexts[i])
    questions[i].setAnswer(answers[i])

print(questions)


