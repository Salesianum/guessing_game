import random

def main():
    playGame()
    
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
    print(guessMe)
    while(ATTEMPTS <= 3):
        userGuess = input("Please enter a guess: ")
        userGuessNum = int(userGuess)
        while(not userGuess.isdigit() or not userGuessNum >= 1 or not userGuessNum <= 100):
            userGuess = input("Please enter a new guess: ")
            userGuessNum = int(userGuess)
        if (give_feedback(guessMe, userGuessNum) == True):
            print(f"Congrats! You won in {ATTEMPTS} tries!")
            break
        ATTEMPTS += 1
    if(ATTEMPTS > 3):
        print(f"You've not yet guessed the correct number. Try again next time...")

if __name__ == "__main__":
    main()