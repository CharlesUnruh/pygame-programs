from abstract_question import Question

class Simple_Question():
    
    __query = None
    __correct_answer = None
    
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
        self.__correct_answer = val
    
    @correct_answer.deleter
    def correct_answer(self):
        del self.__correct_answer
    
    def __init__(self,query,correct_answer):
        self.__query = query
        self.__correct_answer = correct_answer
        
    def isCorrect(self, answer):
        if type(answer) is str:
            answer = answer.lower()
        correct_answer = self.__correct_answer
        if type(correct_answer) is str:
            correct_answer = correct_answer.lower()
        return answer == str(correct_answer)