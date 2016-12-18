from abc import ABCMeta, abstractmethod

class Question(metaclass=ABCMeta):
    
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
    
    @abstractmethod
    def isCorrect(self, answer):
        pass
        