import random


def start_game():

    # Print a text header to welcome the player
    print("---------------------------------------------------------")
    print("Welcome to the number guessing game!")
    print("---------------------------------------------------------")

    # create a  random number
    r_number = random.randint(1,10)
    tries = 0
    print("I'm thinking of a number between 1 and 10")

    guess = input("Enter your guess ")
    # Keep asking to guess the number
    while True:
        #if the guess is right. end loop and sate the number of tries
        if int(guess) == r_number:
            print("Great you got it! It took you", tries, "tries.")
            break
        #if the number that was guessed is lower. Ask to take another guess and add 1 to the tries.
        elif int(guess) < r_number:
            print("You're guess is lower than my number.")
            tries += 1
            guess = input("Try again! Enter a new guess ")
        #if the number is not smaller and not correct then it must be higher. Ask to try again
        else:
            print("You're guess is higer then my number.")
            tries += 1
            guess = input("Try again! Enter a new guess ")




start_game()

print("Game Over! Thanks For Playing!")