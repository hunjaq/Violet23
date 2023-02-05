from Violet23.questionO import question

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
    #make current a question object, default
    current = question()
    #set values of current correctly
    current.setQuestion(qtexts[i])
    current.setAnswer(answers[i])
    current.setType("fr")
    #add object to list
    questions.append(current)

def getList(self):
    return questions

# print(questions[2].getQuestion())


