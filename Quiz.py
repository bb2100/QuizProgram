from random import shuffle

class Question:
    def __init__(self, question:str, trueanswer:str, alternative : list) -> None:
        self.question = question
        self.trueanswer = trueanswer
        self.alternative = alternative

    def check_answer(self, answer):
        if answer == self.trueanswer :
            return 1
        else:
            print(f"That was incorrect. The correct answer was {self.trueanswer}")
        

    def write_alternatives(self):
        print(self.alternative)

class Quiz:
    def __init__(self, name, question : list, score) -> None:
        self.name = name
        self.question = question
        self.score = score

    def ask_question(self):
       ask = shuffle(self.question)
       for x in self.question:
           print (x.question)
           q=0
           for y in x.alternative:
               q+=1
               print(f"{q}: {x}")
            answer = input("Write the letter of the alternative:")
            if y.check_answer(answer) == 1 #Needs controlling answer



    def question_number(self):
        pass

q1 = Question("Hur många bekräftade testiklar har Frej Larsson","c",["a) 1st","b) 2st","c) 3st","d) Inga, bara en manpussy"])

quiz = Quiz("bbsQuiz",[q1],0)



