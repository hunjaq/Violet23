import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.com/career-advice/article/100-potential-interview-questions"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

questions = soup.find_all("div", "li", class_="career-advice-content")

for question in questions:
    with open('output', 'w') as f:
        line = question.text.strip()
        f.write(line + "\n")
