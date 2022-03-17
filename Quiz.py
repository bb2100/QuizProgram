from operator import truediv


class Question:
    def __init__(self, question:str, trueanswer:str, alternative : list) -> None:
        self.question = question
        self.trueanswer = trueanswer
        self.alternative = alternative

    def ask_question(self):
        print(self.question)
        

    def choose_answer(self, answer):
        if answer == self.trueanswer:
            print("You did good")
            return True

        else:
            return False

    def write_alternatives(self):
        print(self.alternative)

class Quiz:
    def __init__(self, name, question : list, score) -> None:
        self.name = name
        self.question = question
        self.score = score

    score = 0

    def question_number(self):
        pass


lis = ["no"]
q1 = Question("What is right?","yes",lis)

q1.ask_question()
q1.choose_answer(input())