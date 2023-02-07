#checks if the user's guess is in the word
def checkGuess(word, guess):
  correct = False
  for char in word:
    if guess == char:
      correct = True
      spot = word.index(guess)
  if correct == True:
    return spot
  else: 
    spot = -1
    return spot
    
def main():
  #initializes the word to be guessed and an empty list 
  word = "hey"
  word_box = []

  #adds _ for each letter in the word to be guessed
  for char in word:
    word_box += "_"
  print(word_box)

  #initializes all needed variables
  lives = 9
  spot = 0
  count = 0
  gameover = False
  wrong_guesses = ""

  #runs while the player hasn't run out of lives
  while lives > 0:
    print()
    guess = input("Enter a letter: ")
    guess = guess.lower()
    spot = checkGuess(word, guess)
    if spot >= 0:
      for i in range(len(word_box)):
        if i == spot:
          answer = word_box.pop(spot)
          answer = word_box.insert(spot, guess)
      count += 1
      print(word_box)
    elif checkGuess(word, guess) == -1:
      print(word_box)
      wrong_guesses += guess + " "
      print(wrong_guesses)
      lives -= 1
      print("Not quite... you have", lives, "lives left")

    #checks if the player has filled up all the possible spaces in the list if so the game ends
    if count == len(word_box):
      print("YOU WIN!! The word was", word.upper())
      # print(word_box)
      break
  #once player runs out of lives the game ends and prints the correct work
  if lives == 0:
    print("GAMEOVER...", "the word was", word.upper())
main()