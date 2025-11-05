#This code starts out by importing an external module called random. then it declares a new function that welcomes the user to the program. Next a new function is declared that takes user imput only accepting whole numbers and asking for the user to enter a whole number again if the imput is invalid. next we declare another function that checks the users guess compared to the correct number and if its too high it informs the user of that and if its too low it informs the user of that, and if its the correct number it ends the code. Finaly we have a play game function that creates a secret number keeps track of the users limited attempts, calls the other functions to make the game run, and loops either untill the user guesses correctly or runs out of attempts. 
import random

def welcome_message():
    print("Welcome to 'Guess the Number' game!")
    print("You have to guess the secret number within a limited number of attempts.")
    print("Let's start!")


def get_guess_input():
    guess = ""
    while guess == "":
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess <= 10 and guess >= 1:
                return guess
            else:
                print("Please guess a number between 1 and 10")
                guess = ""
        except ValueError:
            print("invalid input! Please enter a valid number")
            guess = ""


def check_guess(guess, secret_number, attempts, wrong_guesses):
    if guess > secret_number:
        print("You guessed too high")
        wrong_guesses.append(guess)
        attempts -= 1
        return attempts
    elif guess < secret_number:
        print("You guessed too low")
        wrong_guesses.append(guess)
        attempts -= 1
        return attempts
    
    else:
        print("congratulations! you guessed the secret number!")

def play_game():
    secret_number = random.randint(1,10)
    attempts = 5
    wrong_guesses = []
    welcome_message()
    while attempts > 0:
        print(" \nyou have", attempts, "attempts left.")
        guess = get_guess_input()
        attempts = check_guess(guess, secret_number, attempts, wrong_guesses)
        if guess == secret_number:
            break
        elif attempts == 0:
            print("Game over! The secret number was", secret_number, ". Better luck next time.")
            print("Here are your wrong guesses:")
            print(wrong_guesses)


play_game()