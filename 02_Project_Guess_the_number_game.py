# The game is with computer and a player in which the player guesses the no. of computer and computer states if the random no. is guessed right or wrong!
import random

randNum = random.randint(1, 100)

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

print(f"You guessed the number in {Guesses} guesses.")

with open("Highscore.txt", "r") as f:
    Highscore = int(f.read())

if Guesses < Highscore: 
    print("You have cracked the new Highscore")   
    with open("Highscore.txt", "w") as f:
            f.write(str(Guesses))

    
        