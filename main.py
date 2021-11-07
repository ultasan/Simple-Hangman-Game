import os
import time

player1 = input("What your name: ")
print("ok " + player1 + " the game will start momentarily....")

# Puts a delay

time.sleep(1)


# Clears the screen to make it look good

clear = lambda: os.system('clear')

clear()

temp = "_"
# trueword is word that's supposed to be guessed
trueWord = input(player1 + ", enter a word: ").upper()

#guessCollection to keep track of words guessed

guesses = len(trueWord) + 5
guessCollection = []

#guessword is to keep track of the length of the word and the number of underscores
guessWord = ["_"] * len(trueWord)

isGameComplete = False

clear()

print("THE GAME HAS STARTED")

while not isGameComplete:

  print("".join(guessWord))


  # Letter that player is going to guess

  letterGuess = input(player1 + ", please put your guess: ").upper()


  if len(letterGuess) > 1:
    print("\nYou can only write one letter!\n")

  
  if letterGuess in trueWord:

    guessCollection.append(letterGuess)
  
    for idx, char in enumerate(trueWord):  # go through the word (remembering the index)
  
        if char == letterGuess:             # check if it is a match
  
            guessWord[idx] = letterGuess    # print the result

  elif letterGuess not in trueWord:
    guesses -= 1

    guessCollection.append(letterGuess)
  
    print(f"\nWhoops now you only have {guesses} guesses left!\n")
  
  
  if len(guessCollection) == len(trueWord):
    clear()
    print("YOU HAVE WON THE GAME!")
    isGameComplete = True

  if guesses < 1:
    print("Sorry you died!")
    isGameComplete = True
    
    
    
    