from Violet23.questionO import question

questions = [] #list of question objects
qtexts = [] #list of question strings
answers = [] #string of answers
facts = [] #string of women facts

with open("question.txt", encoding='utf-8') as f:
    for line in f:
        qtexts.append(line.strip())


with open("answers.txt", encoding='utf-8', errors="ignore") as g:
    for line2 in g:
        answers.append(line2.strip())

with open("Facts.txt") as f3:
    for fline in f3:
        facts.append(fline.strip())

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

def getFacts(self):
    return facts
# print(facts[2])
# print(questions[2].getQuestion())


