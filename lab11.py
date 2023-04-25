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
options = []
for i in triviaInfo:
    question = i["question"]
    questionList.append(question)
    optionIndex = i['incorrectAnswers']
    index = random.randint(0,4)
    optionIndex.insert(index, i['correctAnswer'])
    options.append(optionIndex)
 
root = Tk()
root.title("Trivia")
root.geometry("1000x800")

user_answer = StringVar()
user_answer.set("")

count=0
def nextQ():
    global count
    global currentQuestion
    global currentOptions
    currentQuestion = questionList[count]
    currentOptions = options[count]
    question = Label(root, text=currentQuestion,font=('Courier 18')).pack()
    for i in currentOptions:
        labelName = Radiobutton(root, text=i, font=('Courier 12')).pack()
    count+=1

score = 0
def check():
    answer = user_answer.get()
    for i in currentOptions:
        if answer == i:
            correct = Label(root, text="YOU GOT IT!", font=('Courier 10')).pack
    

checkAnswer = Button(root, text="Check Answer", command=check).pack(side=BOTTOM)
nextButton = Button(root, text="Next Question", command=nextQ).pack(side=BOTTOM)
label = Label(root,font=('Courier 18')).pack()

root.mainloop()
