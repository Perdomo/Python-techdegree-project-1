import random

tries = 1
guess = 0
high_score = 9999
play_again = "y"

while play_again == 'y':
    # Print a text header to welcome the player
    print("---------------------------------------------------------")
    print("Welcome to the number guessing game!")
    print("---------------------------------------------------------")

    print(f"The current high score is: {high_score}")
    print("I'm thinking of a number between 1 and 10")

    # create a  random number
    r_number = random.randint(1,10)

    # Keep asking to guess the number
    while guess != r_number:
        guess = input("Enter your guess between 1-10: ")
        try:
            int(guess)
        except:
            print("Make sure you are entering a number from 1-10")
            guess = 0
            tries += 1

        guess = int(guess)

        if guess > 10:
            print("You're guess is not in the range 1-10. Try again!")
            tries += 1
        #if the number that was guessed is lower. Ask to take another guess and add 1 to the tries.
        elif guess < r_number and guess > 0:
            print("You're guess is lower than my number. Try again!")
            tries += 1
        #if the number is not smaller and not correct then it must be higher. Ask to try again
        elif guess > r_number:
            print("You're guess is higher then my number. Try again")
            tries += 1


    print(f"You got it! The number was {r_number}. It took you {tries} tries!")
    if tries < high_score:
        print("New high score!!")
        high_score = tries


    play_again = input("Enter Y to play again ")
    play_again = play_again.lower()



print("Game Over! Thanks For Playing!")