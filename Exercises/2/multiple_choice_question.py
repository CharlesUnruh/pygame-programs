from abstract_question import Question
from random import shuffle
from builtins import int

class Multiple_Choice_Question():
    
    __query = None
    __correct_answer = None
    __answers = None
    
    @property
    def query(self):
        return self.__query
    
    @query.setter
    def query(self, val):
        self.__query = val
    
    @query.deleter
    def query(self):
        del self.__query
        
    @property
    def correct_answer(self):
        return self.__correct_answer
        
    @correct_answer.setter
    def correct_answer(self, val):
        if self.__validate_correct_answer_assignment(val):
            self.__correct_answer = val
    
    @correct_answer.deleter
    def correct_answer(self):
        del self.__correct_answer
    
    @property
    def answers(self):
        if self._random_order:
            shuffle(self.__answers)
        return self.__answers
    
    @answers.setter
    def answers(self, val):
        self.__answers = val
        self.__correct_answer = None
    
    @answers.deleter
    def answers(self):
        del self.__answers



        
    def __validate_correct_answer_assignment(self, val):
        if type(val) is int:
            if val not in range(1,len(self.__answers)+1):
                raise ValueError("Numeral Answer Out Of Range")
            return True
        elif type(val) is str:
            valid_answers = [ answer.lower() for answer in self.__answers]
            valid_answers.extend([chr(ord('a')+i) for i in range(len(self.__answers))])
            if val.lower() not in valid_answers:
                raise ValueError("Answer Not Valid Option")
            return True
        else:
            raise ValueError("Invalid Answer Type")
    
    def __init__(self,query,answers,correct_answer,random_order=False):
        self.__query = query
        self.__answers=answers
        if self.__validate_correct_answer_assignment(correct_answer):
            self.__correct_answer = correct_answer
        self._random_order = random_order
        
    def isCorrect(self, answer):
        print(answer,self.__correct_answer)
        if type(answer) is str:
            answer = answer.lower()
        correct_answer = self.__correct_answer
        if type(correct_answer) is str:
            correct_answer = correct_answer.lower()
        exact_match = answer == correct_answer
        numeral_match = False
        if type(answer) is int:
            numeral_match = self.__answers[answer].lower() == correct_answer
        alpha_match = False
        if type(answer) is str and len(answer) == 1:
            print(self.__answers[ord(answer)-ord('a')])
            alpha_match = self.__answers[ord(answer)-ord('a')].lower() == correct_answer
        return exact_match or numeral_match or alpha_match
        
        