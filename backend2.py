'''
Created on Feb 4, 2023

@author: Darian
'''
from enum import Enum
import string

class Type(Enum):
    mc = 0
    fr = 1

class question(object):
        
    def __init__(self, qType: string, question: string, answer: string):
        if (qType == 'mc'):
            self.qType = Type.mc
        else:
            self.qType = Type.fr
        self.question = question
        self.answer = answer


question1 = question('fr', 'q1', 'a1')
print(question1.qType.name)
print(question1.question)
print(question1.answer)