'''We are going to make a game of hangman.
Rules of the game: 
1. Player 1 AI generates a random word
2. Player 2 guesses these words letter by letter
3. if letter is correct , player 2 places these letters at correct index
4. Else we get a guess again message
5. This will go on till we can guess the correct word'''

import random

# EnterName = input("Enter your name : ")
# Greet = print(f"Hello {EnterName}")

Dictionary = ["lungs","Mug","Noir","Akbar","Jahangir","Jaipur","Oslo","Rajasthan"] # makes the list of small letters
ComputersChoice = random.choice(Dictionary)
lengthOfWord = len(ComputersChoice) #checking the length of the choosen word
print(ComputersChoice,lengthOfWord)

def UserGuess(lengthOfWord, ComputersChoice):
    Userchoice = input("Enter an alphabet : ")
    GuessedWord = "_"*lengthOfWord
    if Userchoice in ComputersChoice:
        index = ComputersChoice.find(Userchoice)
        Guess = GuessedWord.replace((GuessedWord[index],Userchoice))
        print(Guess)
    else:
        print("That's Wrong answer. Try again")
        UserGuess(lengthOfWord, ComputersChoice)
        exit()

UserGuess(lengthOfWord, ComputersChoice)
