class Question:
    def __init__(self, question, trueanswer, alternative : list) -> None:
        self.question = question
        self.trueanswer = trueanswer
        self.alternative = alternative

    def ask_question(self, answer):
        print(self.question)
        answer = input

    def choose_answer(self, answer):
        if answer == self.trueanswer:
            score = score + 1
        
    def write_alternatives(self):
        print(self.alternative)

class Quiz:
    def __init__(self, name, question : list, score) -> None:
        self.name = name
        self.question = question
        self.score = score

    score = 0

    def ask_question(self):
