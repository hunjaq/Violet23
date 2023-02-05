import questionO

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
    current = questionO.question()
    current.setQuestion(qtexts[i])
    current.setAnswer(answers[i])
    current.setType("fr")
    questions.append(current)

# print(questions[2].getQuestion())


