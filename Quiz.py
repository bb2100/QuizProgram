from random import shuffle
from time import sleep

class Question:
    def __init__(self, question:str, trueanswer:str, alternative : list) -> None:
        self.question = question
        self.trueanswer = trueanswer
        self.alternative = alternative

    def check_answer(self, answer): #checks if answer is correct or not
        if answer == self.trueanswer :
            print("Correct! \n")
            return 1
            
        else:
            print(f"That was incorrect. The correct answer was {self.trueanswer} \n")
        

    def write_alternatives(self):
        print(self.alternative)

class Quiz:
    def __init__(self, name, question : list, score=0, qnumber=1) -> None:
        self.name = name
        self.question = question
        self.score = score
        self.qnumber = qnumber

    def ask_question(self):
        ask = shuffle(self.question)
        print(f"\nVälkommen till {self.name}")
        for x in self.question:
            print (f"Question {self.qnumber}\n{x.question}") #Prints the question number and the question
            q=0
            for y in x.alternative:
               q+=1
               print(f"{q}: {y}")
            answer = input("Write the letter of the alternative:").lower()
            if x.check_answer(answer) == 1:
                self.score += 1
                self.qnumber += 1
                print(f"This is your current score: {self.score}\n") #checks right answer and adds and prints the score
            else:
                self.qnumber += 1
                print(f"This is your current score: {self.score}\n") #checks wrong answer and prints score


def get_questions(choice):
    path = ""
    if choice == 1: path="bbs.txt"
    elif choice == 2: path="fakta.txt"

    questions = []
    with open(path, "r", encoding="utf-8") as f:
        name = f.readline() #Reads first line as the quiz name.
        for line in f.readlines():
            question = line.split("/")
            #0 - Question
            #1 - Answer
            #2 - Alternatives
            alts = question[2].split(",")
            questions.append(Question(question[0], question[1], alts))
    quiz = Quiz(name, questions)
    
    return quiz



def main():

    #Below is the thing that chooses quiz and calls for the question
    start = input("Vilket quiz vill du starta? \nSkriv 1 för bbsQuiz\nSkriv 2 för FaktaQuiz\nSkriv nåt annat för att avsluta\n")
    if (start == "1"):
        quiz = get_questions(1)
        quiz.ask_question()
        print ("Det där var sista frågan!\n")
        print (f"Tack för att du spelade {quiz.name}")
        sleep(2)
    if (start == "2"):
        quiz = get_questions(2)
        quiz.ask_question()
        print ("Det där var sista frågan!\n")
        print (f"Tack för att du spelade {quiz.name}")
        sleep(2)
    else:
        raise SystemExit("Programmet Avslutades")

if __name__ == "__main__":
    main()

