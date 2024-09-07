from art import logo
from random import randint

def check_guess(player_guess, answer, turns):
    if player_guess > answer:
        print("Too high.")
        return attempts - 1

    elif answer > player_guess:
        print ("Too low.")
        return attempts - 1

    elif player_guess == answer:
        print (f"You got it! The number is {answer}.")

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")

if difficulty == 'easy':
    attempts = 10

elif difficulty == 'hard':
    attempts = 5

num = randint(1,100)
guess = 0

while guess != num and attempts > 0:

    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: \n"))
    attempts = check_guess(guess, num, attempts)

    if attempts == 0:
        print(f"You ran out of guesses. The number was {num}. You lose.")
        break

    elif guess != num:
        print("Guess again.")



