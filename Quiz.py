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
    def __init__(self, name, question : list, score, qnumber) -> None:
        self.name = name
        self.question = question
        self.score = score
        self.qnumber = qnumber

    def ask_question(self):
        ask = shuffle(self.question)
        for x in self.question:
            print (f"Question {self.qnumber}\n{x.question}") #Prints the question number and the question
            q=0
            for y in x.alternative:
               q+=1
               print(f"{q}: {y}")
            answer = input("Write the letter of the alternative:")
            if x.check_answer(answer) == 1:
                self.score += 1
                self.qnumber += 1
                print(f"This is your current score: {self.score}\n") #checks right answer and adds and prints the score
            else:
                self.qnumber += 1
                print(f"This is your current score: {self.score}\n") #checks wrong answer and prints score



def main(): #Questions and creating quiz
    #quiz 1
    q1_0 = Question("Vilket av dessa spel är bäst enligt bb2100?","b",["a) Cs-Go","b) Overwatch","c) Paper Mario","d) Skyrim"])
    q1_1 = Question("Hur många bekräftade testiklar har Frej Larsson","c",["a) 1st","b) 2st","c) 3st","d) Inga, bara en manpussy"])
    q1_2 = Question("Hur bra är Pussy Lover av DJ Balloon", "a",["a) 11/10","b) 2/10","c) 0/10","d) 6/10"])
    q1_3 = Question("Vad tycker bb2100 om Niclas", "d",["a) Asjobbig", "b) Fett king", "c) För nördig", "d) Daddy <3"])
    q1_4 = Question("Hur uppkom namnet bb2100?","a",["a) Tyckte det lät som robot ca 2013","b) Baserat på starwars bb8","c) Bytte från dd2100","d) Slog nåt random på tangentbordet"])
    q1_5 = Question("Vem hade bb2100 lyssnat mest på 2021?","a",["a) Frej Larsson","b) MF DOOM","c) Terror Reid","d) Johnny Cash"])
    q1_6 = Question("Ja eller nej?","c",["a) Burkmat","b) Nuggets","c) Rättsvar","d) Ja eller nej"])
    q1_7 = Question("Vilken youtuber kollar bb2100 mest på?","d",["a) VSauce","b) Vertasium","c) Markiplier","d) Stamsite"])
    q1_8 = Question("Vilken läsk är bäst?","b",["a) CocaCola","b) CocaCola Vanilla","c) Fanta Strawberry Kiwi","d) DrPepper"])
    q1_9 = Question("NTI Nacka är:","b",["a) Fett nice","b) Sunkigt","c) Lowkey sämst","d) Bäst"])
    
    #quiz 2
    q2_0 = Question("Har delfiner hår?","c",["a) Ja", "b) nej", "c) Bara när dem föds", "d) Bara precis innan dem dör"])

    quiz = Quiz("bbsQuiz",[q1_0,q1_1,q1_2,q1_3,q1_4,q1_5,q1_6,q1_7,q1_8,q1_9],0,1)
    quiz2 = Quiz("FaktaQuiz",[q2_0],0,1)

    #Below is the thing that chooses quiz and calls for the question
    start = input("Vilket quiz vill du starta? \nSkriv 1 för bbsQuiz\nSkriv 2 för FaktaQuiz\nSkriv nåt annat för att avsluta\n")
    if (start == "1"):
        quiz.ask_question()
        print ("Dedär var sista frågan!\n")
        sleep(2)
    if (start == "2"):
        quiz2.ask_question()
        print ("Dedär var sista frågan!\n")
        sleep(2)
    else:
        raise SystemExit("Programmet Avslutades")

if __name__ == "__main__":
    main()

