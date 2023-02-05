'''
Rough draft back-end for quiz

@author: Darian Harrop-Williams

@version: February 4, 2023
'''

import pandas as pd

def play():
    for x in range(frame.__len__()):
        askQuestion(x)
        print()

def askQuestion(questionIndex: int):   

    def askMC():
        print(question)
        if input() == frame.iloc[questionIndex, 2]:
            print('Correct!')
        else:
            print('Incorrect! Correct Answer: ' + frame.iloc[questionIndex,2])
    
    def askFR():
        print(question)
        input()
        print('Suggested Answers: ' + frame.iloc[questionIndex,2])
    
    question = frame.iloc[questionIndex,1]
    qType = frame.iloc[questionIndex,0]
    
    if (qType == 'mc'):
        print('Multiple Choice')
        askMC()
    else:
        print('Free Response')
        askFR()
    

frame  = pd.read_csv('questions.csv')
print(frame)
play()