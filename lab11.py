# Tiffany Ng
import random
from tkinter import *
import requests

#gets json file from trivia API
url = "https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy"
getTrivia = requests.get(url)
triviaInfo = getTrivia.json()
triviaInfo

#makes the list of questions
questionList = []
answerList = []
for i in triviaInfo:
    question = i["question"]
    questionList.append(question)
    for j in range(4):
        section = []
        for k in i['incorrectAnswers']:
            section.append(k)
        correctAns = i["correctAnswer"]
        print(correctAns)
        insertIndex = random.randint(0,4)
    section.insert(insertIndex, correctAns)
    
print(questionList)
print()
print(answerList)


root = Tk()
root.title("Trivia")
root.geometry("1000x800")

count=0
def nextQ():
    global count
    question = Label(root, text=questionList[count],font=('Courier 18')).pack()
    count+=1
    
def check():
    pass

checkAnswer = Button(root, text="Check Answer", command=check).pack(side=BOTTOM)
nextButton = Button(root, text="Next Question", command=nextQ).pack(side=BOTTOM)
label = Label(root,font=('Courier 18')).pack()

root.mainloop()

