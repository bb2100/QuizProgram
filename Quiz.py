from random import shuffle

class Question:
    def __init__(self, question:str, trueanswer:str, alternative : list) -> None:
        self.question = question
        self.trueanswer = trueanswer
        self.alternative = alternative

    def check_answer(self, answer):
        if answer == self.trueanswer :
            print("Correct! \n")
            return 1
            
        else:
            print(f"That was incorrect. The correct answer was {self.trueanswer} \n")
        

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
               print(f"{q}: {y}")
            answer = input("Write the letter of the alternative:")
            if x.check_answer(answer) == 1:
                self.score += 1
                print(f"This is your current score: {self.score}\n")
            else:
                print(f"This is your current score: {self.score}\n")

    def question_number(self):
        pass


def main():
    q1 = Question("Hur många bekräftade testiklar har Frej Larsson","c",["a) 1st","b) 2st","c) 3st","d) Inga, bara en manpussy"])
    q2 = Question("Hur bra är Pussy Lover av DJ Balloon", "a",["a) 11/10","b) 2/10","c) 0/10","d) 6/10"])
    q3 = Question("Vad tycker bb2100 om Niclas", "d",["a) Asjobbig", "b) Fett king", "c) För nördig", "d) Daddy <3"])
    q4 = Question("Hur uppkom namnet bb2100?","a",["a) Tyckte det lät som robot ca 2013","b) Baserat på starwars bb8","c) Bytte från dd2100","d) Slog nåt random på tangentbordet"])

    quiz = Quiz("bbsQuiz",[q1,q2,q3,q4],0)
    quiz.ask_question()
if __name__ == "__main__":
    main()

