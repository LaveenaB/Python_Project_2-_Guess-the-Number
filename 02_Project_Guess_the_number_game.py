# The game is with computer and a player in which the player guesses the no. of computer and computer states if the random no. is guessed right or wrong!
#Step 1: Importing random module for creating random numbers
import random

#Step 2: The player can choose any integer between 1-100 numbers
randNum = random.randint(1, 100)

#Step 3: Inputting the functions to run and print the result
UserGuesses = None
Guesses = 0

while (UserGuesses != randNum):
    UserGuesses = int(input("Enter your number: "))
    Guesses += 1
    if (UserGuesses == randNum):
        print("You guessed it right!")
    else: 
        if (UserGuesses>randNum):
            print("You guessed it wrong!")
            print("Hint: Guess a smaller number")
        else:
            print("You guessed it wrong!")
            print("Hint: Guess a larger number")

#Step 4: Result which states the number of guesses a player could make
print(f"You guessed the number in {Guesses} guesses.")

#Step 5: Set a highscore file with the highscore if the no. of guesses are low
with open("Highscore.txt", "r") as f:
    Highscore = int(f.read())

if Guesses < Highscore: 
    print("You have cracked the new Highscore")   
    with open("Highscore.txt", "w") as f:
            f.write(str(Guesses))

#### Thank you!

    
        