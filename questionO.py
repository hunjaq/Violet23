'''
Created on Feb 4, 2023

@author: Darian
'''

from enum import Enum
import string

#Enum to account for types of questions
class Type(Enum):
    default = 0 #placeholder
    mc = 1 #multiple choice
    fr = 2 #free response

#Question object, has 3 fields
class question(object):
    
    #sets the question type
    def setType(self, qType: string):
        if (qType == 'mc'): #sets enum to mc
            self.qType = Type.mc
        else: # sets enum to fr
            self.qType = Type.fr
        
    #Sets the question
    def setQuestion(self, question: string):
        self.question = question
        
    #Sets the answer
    def setAnswer(self, answer: string):
        self.answer = answer
        
    #Initializes object with default fields
    def __init__(self):
        qType = Type.default
        question = ''
        answer = ''