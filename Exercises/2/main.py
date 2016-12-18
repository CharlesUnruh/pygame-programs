import sys
from multiple_choice_question import Multiple_Choice_Question
from simple_question import Simple_Question

def print_question(question):
    print(question.query)
    print()
    if type(question) is Multiple_Choice_Question:
        answers = question.answers
        for i in range(len(answers)):
            print(chr(ord('a')+i),".) ",answers[i])
        print()

def answer_question(question):
    response = input("Response: ")
    return question.isCorrect(response)

def main(argv):
    questions = []
    questions.append(Multiple_Choice_Question("Who is the Lord of Sunlight?",['Gwenevere','Gwendolin','Allfather Lloyd','Gwen'],'Gwen',random_order=True))
    questions.append(Multiple_Choice_Question("Gwendolin is Gwen's: ",['First Son', 'First Daughter', 'Second Son', 'Second Daughter'],'Second Son'))
    questions.append(Simple_Question("Where did Artorias go to stop the spread of the Abyss?", "Oolacil"))
    questions.append(Simple_Question("How many Bells needed to be tolled?", 2))
    
    number_correct = 0
    number_total = len(questions)
    for question in questions:
        print_question(question)
        if answer_question(question):
            number_correct += 1
            
    print("Your score: ", number_correct/number_total)
    

main(sys.argv)

            
