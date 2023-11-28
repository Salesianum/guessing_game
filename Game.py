import random

def main():
    play = True
    while(play == True):
        playGame()
        handleInput = input("Would you like to play again? (y/n) ").lower()
        while(handleInput != "y" and handleInput != "n"):
            handleInput = input("Please enter y or n to answer... ").lower()

        if (handleInput == "n"):
            play = False
        
def playerGuess():
    return(input("Please enter your guess: "))


def generate_random_number():
    return (random.randint(1, 100))

def give_feedback(secret_number, guess):
    if(secret_number < guess):
        print("You need to guess a smaller number...")
        return(False)
    elif(secret_number > guess):
        print("You need to guess a bigger number...")
        return(False)
    else:
        print("Hey! You got it right!")
        return(True)

def playGame():
    ATTEMPTS = 1;
    guessMe = generate_random_number()
    while(ATTEMPTS <= 3):
        userGuess = playerGuess()
        userGuessNum = int(userGuess)
        while(not userGuess.isdigit() or not userGuessNum >= 1 or not userGuessNum <= 100):
            userGuess = playerGuess()
            userGuessNum = int(userGuess)
        if (give_feedback(guessMe, userGuessNum) == True):
            print(f"Congrats! You won in {ATTEMPTS} attempt(s)")
            break
        ATTEMPTS += 1
    if(ATTEMPTS > 3):
        print(f"You've not yet guessed the correct number. It was {guessMe}. Try again next time...")

if __name__ == "__main__":
    main()