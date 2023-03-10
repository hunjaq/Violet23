'''
Created on Feb 4, 2023

@author: Darian
'''

from enum import Enum
import string


# Enum to account for types of questions
class Type(Enum):
    default = 0  # placeholder
    mc = 1  # multiple choice
    fr = 2  # free response


# Question object, has 3 fields
class question(object):
    qType = 0
    answer = ""
    question = ""

    # sets the question type
    def setType(self, qType: string):
        if (qType == 'mc'):  # sets enum to mc
            self.qType = 1
        else:  # sets enum to fr
            self.qType = 2
        
    # Sets the question
    def setQuestion(self, question: string):
        self.question = question
        
    # Sets the answer
    def setAnswer(self, answer: string):
        self.answer = answer

    def getQuestion(self):
        return self.question
    
    def getAnswer(self):
        return self.answer
        
    def getQType(self):
        return self.qType

    # Initializes object with default fields
    def __init__(self):
        self.qType = 0
        self.question = ''
        self.answer = ''
