# Tiffany Ng
from tkinter import *
import json
import requests
# retrieves 20 random quotes and its additional information from the api
url = "https://api.quotable.io/quotes/random?limit=20"
randomQ = requests.get(url)
randomQuotesJSON = randomQ.json()
randomQuotesJSON

# creates a list of the 20 randomly selected authors
authors = []
for i in range(20):
    authors.append(randomQuotesJSON[i]['author'])
print(authors)

# creates the GUI
quoteGUI = Tk()

# this function sets up a new random list of 20 authors
def generate():
    url = "https://api.quotable.io/quotes/random?limit=20"
    randomQ = requests.get(url)
    randomQuotesJSON = randomQ.json()
    randomQuotesJSON
    authors = []
    for i in range(20):
        authors.append(randomQuotesJSON[i]['author'])
    print(authors)
        
# this function is associated with the "click me" button
# when clicked it checks which author the user chose and returns the corresponding quote they stated
def show():
    for i in range(20):
        if clicked.get() == authors[i]:
            quote = randomQuotesJSON[i]['content']
    label.config(text=quote)          

clicked = StringVar()
clicked.set(authors[0])

# creates the drop down menu and initializes it with the 20 authors 
drop = OptionMenu(quoteGUI, clicked, *authors)
drop.config(width=20)
drop.pack() 

# creates the necessary button functions
button = Button(quoteGUI, text= "click me", command = show).pack()
button = Button(quoteGUI, text= "new list", command = generate).pack()
label = Label(quoteGUI, text= " ")
label.pack()

quoteGUI.mainloop()
