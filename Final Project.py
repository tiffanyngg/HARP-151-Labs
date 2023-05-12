import requests
import random
import json

#converts the genre chosen by the user to its id defined in TMDB API
#returns: the id for the corresponding genre, used to obtain more data for a specific genre
def genre_to_id(api_key, genre):
    url_genre = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_file = requests.get(url_genre)
    genreJSON = genre_file.json()

    genreId = ""
    for i in genreJSON['genres']:
        if genre == i['name']:
            genreId = i['id']
            return genreId
        
#returns: a list of movie ids within the users' given parameters
#reference: https://flexiple.com/python/python-list-contains/#
#           used to avoid duplicate movie ids in recommendation list
def movie_rec_list(api_key,genreID, year):
    movie_recs_id = []
    for i in range (5):
        page = random.randrange(1,20)
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&page=1&with_genres={genreID}&with_original_language=en&primary_release_year={year}"
        file = requests.get(url)
        fileJSON = file.json()
        for i in fileJSON['results']:
            movieID = i['id']
            if movie_recs_id.count(movieID) > 0:
                pass
            else:
                movie_recs_id.append(movieID)
    return movie_recs_id

#returns: a list of 5 randomly chosen movies from the larger list 
def random_five(movieList):
    shortenMovieList = []
    for i in range(5):
        movie = random.choice(movieList)
        shortenMovieList.append(movie)
        movieList.remove(movie)
    return shortenMovieList

#takes a list of movie ids and retrieves its movie name
#returns: a list of movie names 
def ids_to_titles(movieList):
    movie_titles = []
    for i in range(len(movieList)):
        movieID = movieList[i]
        url = f"https://api.themoviedb.org/3/movie/{movieID}?api_key=dbebf8332d7f2a6a7b46a3d975fb656a&language=en-US&with_original_language=en"
        movieFile = requests.get(url)
        movieJSON = movieFile.json()
        movie_titles.append(movieJSON['original_title'])
    return movie_titles

#takes the shorten list and retrieves the actors & actresses that are in the movie
def movie_cast(shortenMovieList):
    global cast
    cast = []
    castIDS = []
    for i in range(len(shortenMovieList)):
        movieID = shortenMovieList[i]
        #initiates a new json for the specified information
        url = f"https://api.themoviedb.org/3/movie/{movieID}/credits?api_key=dbebf8332d7f2a6a7b46a3d975fb656a&language=en-US"
        movieInfo = requests.get(url).json()
        #print(movieInfo)
        for j in movieInfo['cast']:
            cast.append(j['name'])
    return castIDS

#get movieID from name
# def getID(movieName, movieIDList):
#     for i in range(len(movieIDList)):
#         if movieName == 


#initializes GUI window
from tkinter import *
root = Tk()
root.geometry('700x600')
root.title("BTK2 Movie Generator")
root['background'] = "#AFBBF2"
Label(text=".•*•.BTK2 Movie Generator.•*•.", font=("Comic Sans MS", 50, "bold"), bg="#AFBBF2", fg="#4E598C").grid(row=0, column=0)

#creates prompt to guide user to choose from the available genres
Label(text="Select a genre: ", font=('Ariel', 20, 'bold'), bg="#AFBBF2", fg="#4E598C").grid(row=1, column=0)
genres = ['Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Horror', 'History', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']
clicked = StringVar()
clicked.set('genre')

#creates drop down menu with all the genres
drop = OptionMenu(root, clicked, *genres)
drop.config(width=20)
drop.grid(row=2, column =0)


#asks user input for year of release thru drop down menu
Label(root, text="Type in a year (ex.1999), but do not exceed current year:", font = ('Ariel', 20, 'bold'), bg="#AFBBF2", fg="#4E598C").grid(row=3, column=0)
years = []
year = 2023
for i in range(74):
    years.append(year)
    year-=1
clickedYear = StringVar()
clickedYear.set('year')
dropYear = OptionMenu(root, clickedYear, *years)
dropYear.config(width=20)
dropYear.grid(row=4, column=0)

#main function that calls on all previously defined functions that uses TMDB API
def main():
    root.config(cursor="star")
    key = "dbebf8332d7f2a6a7b46a3d975fb656a"
    genre = clicked.get()
    genreID = genre_to_id(key, genre)
#     print(genreID)
    year = clickedYear.get()
#     print(year)
    global movieList
    movieList = movie_rec_list(key, genreID, year)
    print(movieList)
    global movies
    movies = random_five(movieList)
    print(movies)
    global names
    names = ids_to_titles(movies)
    print(names)
    global castIDS 
    castIDS = movie_cast(movies)
    print(castIDS)
    
    #asks for user input on the actors/actress they'd like to watch
    #based on the shorter movie list, where the cast members are retrieved from each movie id
    Label(text="Who would you like to see: ", font=('Ariel', 20, 'bold'), bg="#AFBBF2", fg="#4E598C").grid(row=5, column=0)
    
    #creates drop down menu with for actors&actresses
    global celebrity
    clickedActor = StringVar()
    clickedActor.set('actor/actress')
    celebrity = clickedActor.get()
    dropActor = OptionMenu(root, clickedActor, *cast)
    dropActor.config(width=20)
    dropActor.grid(row=6, column =0)
main()

#button that calls on main function to run after all inputs have been gathered
confirm = Button(root, text = "Confirm", command = main)
confirm.grid(row=7,column=0)

#takes the list of movies from the main function and labels each one onto the GUI
def print_recs():
    Label(root, text="Recommendations", font= ('Ariel', 23, "bold"), bg="#AFBBF2", fg="#5AAA95").grid(row=0, column=1)
    for i in range(len(names)):
        recs_label = Label(root, text=names[i], font=('Ariel', 20), bg="#AFBBF2", fg="#4E598C").grid(row=i+1, column=1)
output = Button(root, text = "Results", command = print_recs)
output.grid(row=7, column=1)

#work in progress: intended to clear the recommendation texts to make way for new recommendations of a
#different time and genre
# def clear():
#     recs_label.config(text=" ")
# refresh = Button(root, text="Clear", command=clear)
# refresh.grid(row=7, column=3)

#generates another list of movie recommendations under the same parameters
def again():
    Label(root, text="More Recommendations", font= ('Ariel', 23, 'bold'), bg="#AFBBF2", fg="#5AAA95").grid(row=8, column=1)
    movies = random_five(movieList)
    names = ids_to_titles(movies)
    for i in range(len(names)):
        Label(root, text=names[i], font=('Ariel', 20), bg="#AFBBF2", fg="#4E598C").grid(row=i+9, column=1)
        
#https://www.geeksforgeeks.org/changing-the-mouse-cursor-tkinter/
#change cursor for aesthetics
root.config(cursor="star")
more = Button(root, text="More Recomendations", command = again)
more.grid(row=15, column=1)
root.mainloop()
