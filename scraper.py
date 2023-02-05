import requests
from bs4 import BeautifulSoup

URL = "https://www.themuse.com/advice/interview-questions-and-answers"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

questions = soup.find_all(class_="inline")
for question in questions:
    with open('output2', 'w') as f:
        line = question.text.strip()
        #f.write(line + "\n")
        #print(question.text.strip(), end = "\n")

answersPart = soup.find_all("div", "div", "p", class_="article-body__content-module")[0]
# answers = answersPart.find_all("p")[4]

for answer in answersPart:
    with open('answers(50)', 'w') as g:
        line = question.text.strip()
        g.write(line + "\n")
        print(answer.text.strip(), end = "\n")

